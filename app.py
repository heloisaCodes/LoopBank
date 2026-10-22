import json
import os
from flask import Flask, render_template, request, redirect, url_for
from procurar import procurarCliente, procurarPorCpf
from conta import autenticar, cadastrarConta, excluirContasSemCliente
from cliente import cadastrarCliente, validarCpf, excluirCliente, editarCliente
from agencia import receberAgencia, agencias 
from relatorio import gerarDashboard
from conta_corrente import criarContaCorrente
from conta_poupanca import criarContaPoupanca
from conta_salario import criarContaSalario
from relatorio import (
    montanteBanco,
    montanteAgencia,
    maiorSaldo,
    menorSaldo
)
from functools import reduce




app = Flask(__name__) #cria a aplicação web

#aqui é o filtro pra mostrar dinheiro no formato brasileiro
@app.template_filter("brl")
def brl(valor):
    texto = f"{valor:,.2f}"      #1234.5 vira "1,234.50" (formato americano)
    #troca a virgula por X, o ponto por virgula e o X por ponto,   ex: "1.234,50"
    return texto.replace(",", "X").replace(".", ",").replace("X", ".")


# Nome do arquivo onde os dados serão salvos
ARQUIVO_DADOS = 'dados.json'

# Função para carregar clientes e contas a partir de um arquivo JSON
def carregar_dados():
    """Lê a lista de clientes e contas salva no arquivo JSON."""
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, 'r', encoding='utf-8') as f:
            conteudo = f.read().strip()

            if not conteudo:
                return {"clientes" : [], "contas" : []}
            return json.loads(conteudo)
    return {"clientes": [],
            "contas": []}
#essa função foi adaptada pra evitar que um arquivo vazio cause algum erro no futuro 


# Função para salvar clientes e contas em um arquivo JSON
def salvar_dados(dados):
    """Salva a lista de clientes e contas no arquivo JSON."""
    with open(ARQUIVO_DADOS, 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

dados = carregar_dados()
clientes = dados['clientes']
contas = dados['contas']


@app.route('/') #primeira rota - pagina inicial
def inicio():
    return render_template('index.html') #devolve o arquivo html


@app.route('/cadastro', methods=['POST', 'GET']) #o cliente se cadatra
def cadastroCliente():
    if request.method == 'GET':  #mostra o formulário 
        return render_template('cadastro.html') #devolve o arquivo html

    nome = request.form.get('nome')
    cpf = request.form.get('cpf')     #pega os dados digitados
    senha = request.form.get('senha')
    tipo = request.form.get('tipo')


    if not validarCpf(cpf): #vẽ se o cpf segue o padrão certo, caso não, retorna a pagina de cadastro com a mensagem de erro
        return render_template(
        'cadastro.html',
        erro='CPF inválido.'
    )

    tiposdeConta = ['corrente', 'poupança', 'salario']
    if tipo not in tiposdeConta:
        return render_template(
            'cadastro.html',
            mensagem='Selecione um tipo de conta válido.'
        )

    cliente = cadastrarCliente(clientes, cpf, nome) #procura o cliente pelo cpf dado

    if not cliente: #se o cliente existe retorna falso, então não falso = verdadeiro
        clienteCadastrado = procurarCliente(clientes, cpf)
        return redirect(url_for(
            'entrarConta',
              cpf=cpf,                                #caso do cliente já cadastrado = vai para a pagina de login 
              mensagem='Este CPF já está cadastrado.',
              nome=clienteCadastrado['nome']
              )) 
    
    agencia = receberAgencia(clientes, cpf, agencias, contas)
    contaCliente = cadastrarConta(contas, senha, cpf, agencia)

    if contaCliente:  #cadastro bem sucedido
        novaConta = contas[-1]  #pega a ultima conta cadastrada, que é a nova conta

        if tipo == 'corrente':
            criarContaCorrente(novaConta)  #cria a conta corrente
        elif tipo == 'poupança':
            criarContaPoupanca(novaConta)  #cria a conta poupança
        elif tipo == 'salario':
            criarContaSalario(novaConta)  #cria a conta salário

        
        salvar_dados({
            'clientes': clientes,   #salva os dados
            'contas': contas
            })
        
        return redirect(url_for('areaCliente'))  #vai para a area do cliente, entra no banco



@app.route('/login', methods=['GET', 'POST']) #ou faz o login
def entrarConta():
    if request.method == 'GET':  #mostra a pagina
        return render_template('login.html')

    cpf = request.form.get('cpf')                  #pega os dados dos clientes
    senhadigitada = request.form.get('senha')

    if not validarCpf(cpf): #vẽ se o cpf segue o padrão certo, caso não, retorna a pagina de cadastro com a mensagem de erro
        return render_template(
        'login.html',
        erro='CPF inválido.'
    )

    cliente = procurarCliente(clientes, cpf)  #cliente com respectivo cpf
    contasCliente = procurarPorCpf(contas, cpf) #procura as contas do cliente pelo cpf

    if cliente:            #cliente já está cadastrado
        contasCorrespondentes = []

        for conta in contasCliente:  #verifica todas as contas do cliente
            verificasenha = autenticar(conta, senhadigitada) #autenticar está fazendo a comparação

            if verificasenha: #se a senha digitada for igual a senha da conta
                contasCorrespondentes.append(conta) #então adiciona a conta na lista de contas correspondentes

        if len(contasCorrespondentes) == 1:  #a senha pertence a apenas 1 conta
            return render_template(
                'cliente.html',
                conta=contasCorrespondentes[0],  #entra na conta especifica
                cliente=cliente                 
            )

        elif len(contasCorrespondentes) > 1: #mais de 1 conta possui a mesma senha ps: em conta.py nas funções referentes não tem nenhuma restrição de senha
            return render_template(
                'selecionar_conta.html',      #mostra a lista de contas do cliente (com a mesma senha)
                contas=contasCorrespondentes,
                cpf=cpf
            )

        else:  #senha errada, tenta dnv
            return render_template(
                'login.html',
                mensagem='Senha incorreta.'
            )

    else:  #cliente não está cadastrado
        return redirect(url_for('cadastroCliente')) #vai para cadastro
    

@app.route('/area_cliente') #pagina do cliente
def areaCliente():
    cpf = request.args.get('cpf')              #pega os dados pelo url
    numeroConta = request.args.get('numerodaconta')

    cliente = procurarCliente(clientes, cpf)   
    contasCliente = procurarPorCpf(contas, cpf)

    conta = None 

    for c in contasCliente: #pecorre todas as contas do cliente, até achar a conta com o numero da conta digitada
        if str(c['numerodaconta']) == str(numeroConta):
            conta = c

    if cliente and conta: #encontrou o cliente e a conta?
        return render_template('cliente.html', cliente=cliente, conta=conta) #então abre a área do cliente com os dados atualizados

    return redirect(url_for('entrarConta')) #caso contratrio, volta para a pagina de login

@app.route('/selecionar_conta', methods=['POST']) #pagina de seleção de conta
def selecionarConta():
    cpf = request.form.get('cpf')
    senhaDigitada = request.form.get('senha')   #pega os dados do cliente
    numeroConta = request.form.get('numero da conta')

    contasCliente = procurarPorCpf(contas, cpf)
    contasCorrespondentes = []

    for conta in contasCliente:
        verificaSenha = autenticar(conta, senhaDigitada)

        if verificaSenha:
            contasCorrespondentes.append(conta)

    for conta in contasCorrespondentes:
        if str(conta['numerodaconta']) == numeroConta:   #identifica o número da conta escolhida 
            return render_template(
                'cliente.html',
                conta=conta,                   
                cliente=procurarCliente(clientes, cpf) 
            )

    return redirect(url_for('entrarConta'))  #rediceriona o cliente para a área do cliente daquela conta.


@app.route('/excluir_cliente', methods=['POST']) #exclui o cliente
def excluirCadastro():
    cpf = request.form.get('cpf') #pega o cpf do cliente a ser excluido

    exclusao = excluirCliente(cpf, clientes, contas) #chama a função

    if exclusao: #se excluiu
        excluirContasSemCliente(contas, cpf) #chama a função para excluir a conta, se ela estiver sem clientes

        salvar_dados({
            'clientes': clientes,     #salva as alterações
            'contas': contas
        })

    return redirect(url_for('inicio')) #volta para o inicio


@app.route('/editar_cliente', methods=['GET', 'POST'])
def editarNome():
    if request.method == 'POST':
        cpf = request.form.get('cpf')        #pega os dados
        novoNome = request.form.get('nome')

        resultado = editarCliente(clientes, cpf, novoNome) #chama a função

        if resultado: #se a edição foi bem sucedida
            salvar_dados({
                'clientes': clientes,  #salva as alterações
                'contas': contas
            })

        
    numeroConta = request.form.get('numerodaconta') #pega o numero da conta

    return redirect(url_for(
        'areaCliente',             #fica na pagina do cliente, mas com o nome editado
        cpf=cpf,
        numerodaconta=numeroConta
    ))



@app.route("/gerente/dashboard")
def dashboard_gerente():
    
    dados_arquivo = carregar_dados()                     #carrega os dados do json

    
    clientes = dados_arquivo.get("clientes", [])        #pega as listas atuais do sistema
    contas = dados_arquivo.get("contas", [])

    
    indicadores = gerarDashboard(clientes, contas)          #faz os calculos

                                                            #envia os resultados do python para o HTML
    return render_template(
        "dashboard.html",
        dados=indicadores
    )

if __name__ == '__main__':
    app.run(debug=True)



@app.route('/relatorio')   #rota de relatorio
#carrega os dados salvos e pega a lista de contas
def pagina_relatorio():
    dados_relatorio = carregar_dados()
    contas_relatorio = dados_relatorio.get('contas', [])

    #calcula os numeros do resumo do banco
    montante_banco = montanteBanco(contas_relatorio)  #soma de todos os saldos
    maior_saldo = maiorSaldo(contas_relatorio)        #maior saldo entre as contas
    menor_saldo = menorSaldo(contas_relatorio)        #menor saldo entre as contas

    #calcula, por agencia, a quantidade de clientes e o montante
    #o montante é o que vira o tamanho de cada barra no grafico
    if agencias:
        resultados_agencias, agencia_maior = montanteAgencia(
            contas_relatorio, agencias
        )
    else:
        resultados_agencias = []   #sem agencias cadastradas, o relatorio mostra as mensagens de "vazio"
        agencia_maior = None

    #manda tudo pra o gerente.html desenhar a pagina
    return render_template(
        'gerente.html',
        montante_banco=montante_banco,
        maior_saldo=maior_saldo,
        menor_saldo=menor_saldo,
        resultados_agencias=resultados_agencias,
        agencia_maior=agencia_maior
    )



