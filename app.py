import json
import os
import math
from flask import Flask, render_template, request, redirect, url_for
from conta import Conta
from cliente import Cliente
from agencia import Agencia
from conta_corrente import ContaCorrente
from conta_poupanca import ContaPoupanca


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
                return {"clientes" : [],
                         "contas" : []}
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
clientes = [                    #transforma o dicionario em objetos e armazena na lista 
    Cliente.deDicionario(dados) #método da classe cliente
    for dado in dados['clientes']
                 ]
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

    #dados da conta salário
    empresa = request.form.get('empresa')
    cnpj = request.form.get('cnpj')
    salario = request.form.get('salario')

    if not Cliente.validarCpf(cpf): #vẽ se o cpf segue o padrão certo, caso não, retorna a pagina de cadastro com a mensagem de erro
        return render_template(
        'cadastro.html',
        erro='CPF inválido.'
    )


    clienteCadastrado = Agencia.procurarCliente(cpf)

    if clienteCadastrado:
        return redirect(url_for(
            'entrarConta',
            cpf=cpf,
            mensagem='Este CPF já está cadastrado.',
            nome=clienteCadastrado.nome
        ))

    novoCliente = Cliente(cpf, nome)
    Agencia.adicionarCliente(novoCliente)
    
    # agencia = receberAgencia(clientes, cpf, agencias, contas)
    # contaCliente = cadastrarConta(contas, senha, cpf, agencia)

    # if contaCliente:  #cadastro bem sucedido
    #     novaConta = contas[-1]  #pega a ultima conta cadastrada, que é a nova conta

    #     if tipo == 'corrente':
    #         criarContaCorrente(novaConta)  #cria a conta corrente
    #     elif tipo == 'poupança':
    #         criarContaPoupanca(novaConta)  #cria a conta poupança
    #     elif tipo == 'salario':
    #         criarContaSalario(novaConta, empresa, salario, cnpj)  #cria a conta salário

        
    #     salvar_dados({
    #         'clientes': clientes,   #salva os dados
    #         'contas': contas
    #         })
        
    #     return redirect(url_for('areaCliente'))  #vai para a area do cliente, entra no banco


@app.route('/login', methods=['GET', 'POST'])
def entrarConta():
    if request.method == 'GET':  # Mostra a página de login
        return render_template('login.html')

    cpf = request.form.get('cpf')                  
    senhadigitada = request.form.get('senha')

    if not Cliente.validarCpf(cpf):  #Vê se o CPF segue o padrão certo
        return render_template(
            'login.html',
            erro='CPF inválido.'
        )

    cliente = Agencia.procurarCliente(clientes, cpf)  
    contasCliente = Agencia.procurarPorCpf(contas, cpf) 

    if cliente:  #Cliente já está cadastrado
        contasCorrespondentes = []

        
        # for conta in contasCliente:  
        #     verificasenha = autenticar(conta, senhadigitada) #verifica a senha

        #     if verificasenha:  #Se a senha digitada for igual à senha da conta
        #         contasCorrespondentes.append(conta) #adiciona a correspondentes

        # if len(contasCorrespondentes) == 1:  #A senha pertence a apenas 1 conta
        #     contaUnica = contasCorrespondentes[0]
            
        #     if contaUnica['tipo'] == 'corrente': #entra na conta correspondente
        #         return render_template(
        #             'area_corrente.html',
        #             cliente=cliente,
        #             conta=contaUnica
        #         )

        #     else contaUnica['tipo'] == 'poupança':
        #         return render_template(
        #             'area_poupanca.html',
        #             cliente=cliente,
        #             conta=contaUnica
        #         )

        # elif len(contasCorrespondentes) > 1:  #Mais de 1 conta possui a mesma senha
        #     return render_template(
        #         'selecionar_conta.html',      
        #         contas=contasCorrespondentes,
        #         cpf=cpf,
        #         cliente=cliente
        #     )

        else:  #Senha errada
            return render_template(
                'login.html',
                mensagem='Senha incorreta.'
            )

    else:  #Cliente não está cadastrado
        return redirect(url_for('cadastroCliente'))
    

@app.route('/area_cliente') #pagina do cliente
def areaCliente():
    cpf = request.args.get('cpf')              #pega os dados pelo url
    numeroConta = request.args.get('numerodaconta')

    cliente = Agencia.procurarCliente(cpf)   
    contasCliente = Agencia.procurarPorCpf(cpf)

    conta = None 

    for c in contasCliente: #pecorre todas as contas do cliente, até achar a conta com o numero da conta digitada
        if str(c['c.numeroConta']) == str(numeroConta):
            conta = c

    # if cliente and conta: #encontrou o cliente e a conta?
    #     if conta['tipo'] == 'corrente': #entra na área da conta correspondente
    #        return render_template(
    #            'area_corrente.html',
    #             cliente=cliente,
    #             conta=conta
    #             ) 
    #     elif conta['tipo'] == 'poupança':
    #         return render_template(
    #             'area_poupanca.html',
    #               cliente=cliente,
    #                 conta=conta
    #                 )
    #     else:
    #         return render_template(
    #             'area_salario.html',
    #               cliente=cliente,
    #                 conta=conta
    #                 )

    # return redirect(url_for('entrarConta')) #caso contratrio, volta para a pagina de login

@app.route('/selecionar_conta', methods=['POST'])
def selecionarConta():
    cpf = request.form.get('cpf')
    numeroConta = request.form.get('numeroConta')

    
    contasCliente = Agencia.procurarPorCpf(contas, cpf) 
    cliente = Agencia.procurarCliente(clientes, cpf)
    
    contaEscolhida = None

    #aqui verifica qual conta ele escolheu ao clicar no botao
    for conta in contasCliente:
        if str(conta['numerodaconta']) == str(numeroConta):
            contaEscolhida = conta #pega a conta especifica

    
    # if cliente and contaEscolhida:  #se encontrou o cliente e a conta correspondente
    #     tipo_conta = contaEscolhida.get('tipo')
        
    #     if tipo_conta == 'corrente': #redireciona para a respetiva área
    #         return render_template(
    #             'area_corrente.html',
    #             cliente=cliente,
    #             conta=contaEscolhida
    #         )

    #     else tipo_conta == 'poupança':
    #         return render_template(
    #             'area_poupanca.html',
    #             cliente=cliente,
    #             conta=contaEscolhida
    #         )

    # Se por algum motivo a conta não for encontrada, recarrega a página mostrando as contas
    return render_template(
        'selecionar_conta.html',
        contas=contasCliente,
        cpf=cpf,
        cliente=cliente,
        erro='Conta inválida ou erro ao selecionar.'
    )
    
@app.route('/excluir_cliente', methods=['POST'])
def excluirCadastro():
    cpf = request.form.get('cpf')

    Agencia.excluirCliente(cpf)

    return redirect(url_for('inicio'))


@app.route('/editar_cliente', methods=['GET', 'POST'])
def editarNome():
    if request.method == 'POST':
        cpf = request.form.get('cpf')
        novoNome = request.form.get('nome')

        resultado = Agencia.editarCliente(cpf, novoNome)


    numeroConta = request.form.get('numerodaconta')

    return redirect(url_for(
        'areaCliente',
        cpf=cpf,
        numerodaconta=numeroConta
    ))




# cada tipo de conta aponta pra sua classe
# assim, na hora de criar a conta, nao precisa de um monte de if 
CLASSE_POR_TIPO = {
    'corrente': ContaCorrente,
    'poupanca': ContaPoupanca

}

# FUNÇÕES AUXILIARES

def normalizarTipo(tipo):
    # tipo "Poupança" vira "poupanca"
    tipo = (tipo or '').lower()
    return tipo.replace('á', 'a').replace('ç', 'c')


def lerValor(texto):
    # transforma o que a pessoa digitou em número, tipo '1.250,50' vira 1250.5
    texto = (texto or '').strip().replace('R$', '').replace(' ', '')   # tira o R$ e os espacos

    if ',' in texto:                                  # formato brasileiro
        texto = texto.replace('.', '').replace(',', '.')

    try:
        valor = float(texto)
    except ValueError:                                # digitou letras, por exemplo
        return None

    if not math.isfinite(valor):                      # bloqueia "nan" e "inf"
        return None

    return round(valor, 2)                            # arredonda pra 2 casas decimais, por conta dos centavos


def gerarNumeroConta():  # gera o numero da proxima conta, o maior numero que ja existe + 1
    # default=0 faz funcionar tambem quando ainda nao tem nenhuma conta (ent a primeira vira 1)
    return max((conta.numeroConta for conta in agencia.contas), default=0) + 1


def buscarContaDoCliente(cpf, numeroConta):  # procura, entre as contas daquele cpf, a que tem o número informado
    for c in agencia.procurarContasCliente(cpf):      # percorre as contas da agencia
        if c.cpf == cpf and str(c.numeroConta) == str(numeroConta):   # str() porque o numero da URL vem como texto
            return c                                              # achou: devolve o objeto conta
    return None                                                   # nao achou
    


def valorDisponivel(conta):  # quanto a pessoa pode movimentar na conta (antes era o DISPONIVEL_POR_TIPO)
    # na corrente é saldo + limite (ex: saldo 100 + limite 500 = 600), na poupanca é so o saldo
    if hasattr(conta, 'limite_disponivel'):       # só a ContaCorrente tem esse método
        return conta.limite_disponivel()
    return conta.saldo



# ROTAS

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



@app.route('/nova_conta', methods=['GET', 'POST'])
def criarNovaConta():
    cpf = request.args.get('cpf')                 # pega o cpf da URL
    cliente = agencia.procurarCliente(cpf)        # devolve o objeto Cliente (ou False se nao achar)

    if not cliente:                               # cpf que nao existe na agencia
        return render_template('nova_conta.html', cliente=None, erro='Cliente não encontrado.')

    if request.method == 'GET':                   # so abriu a pagina: mostra o formulario
        return render_template('nova_conta.html', cliente=cliente)

    tipo = normalizarTipo(request.form.get('tipo_conta'))    # tipo escolhido
    senha = request.form.get('senha')
    confirmarSenha = request.form.get('confirmar_senha')

    if senha != confirmarSenha:                   # verifica se a senha é a mesma nos dois campos
        return render_template(
            'nova_conta.html',
            cliente=cliente,
            erro='As senhas não coincidem'
        )

    if tipo not in CLASSE_POR_TIPO:               # tipo invalido, pois o antigo "salario" nao existe mais
        return render_template(
            'nova_conta.html',
            cliente=cliente,
            erro='Tipo de conta inválido'
        )

    classeConta = CLASSE_POR_TIPO[tipo]           # pega a classe certa (ContaCorrente ou ContaPoupanca)
    numero = gerarNumeroConta()                   # numero novo pra conta

    # cria o OBJETO da conta já do tipo certo
    #antes eram 2 passos: cadastrarConta e depois criarContaCorrente/criarContaPoupanca
    # a Conta recebe "cliente" e "cpf" separados e imprime o "cliente" como nome
    # por isso aqui passo cliente.nome se a conta passar a guardar o objeto Cliente
    novaConta = classeConta(cliente.nome, cpf, numero, senha=senha)

    agencia.adicionarConta(novaConta)             # coloca a conta na lista de contas da agência


    return redirect(url_for(
        'areaCliente',
        cpf=cpf,                                  # vai para a area do cliente
        numerodaconta=novaConta.numeroConta       # agora é atributo do objeto, nao mais chave de dicionario
    ))


@app.route("/gerente/dashboard")
def dashboard_gerente():
    # NAO carrega mais o json aqui, porque os dados ja estao na agencia, em memória

    # usar agencia.clientes e agencia.contas, também trocar conta['saldo'] por conta.saldo
    indicadores = gerarDashboard(agencia)         # faz os calculos

    # envia os resultados do python para o HTML
    return render_template(
        "dashboard.html",
        dados=indicadores
    )


@app.route('/relatorio')   # rota de relatorio
def pagina_relatorio():

    if agencia.contas:
        montante_banco = agencia.montante()       # soma de todos os saldos
        maior_saldo = agencia.maiorSaldo()        # maior saldo entre as contas
        menor_saldo = agencia.menorSaldo()        # menor saldo entre as contas
    else:
        montante_banco = 0
        maior_saldo = 0
        menor_saldo = 0

    # por enquanto mando vazio so pra nao quebrar o gerente.html
    resultados_agencias = []
    agencia_maior = None

    # manda tudo pro gerente.html desenhar a pagina
    return render_template(
        'gerente.html',
        montante_banco=montante_banco,
        maior_saldo=maior_saldo,
        menor_saldo=menor_saldo,
        total_clientes=agencia.quantidadeClientes(),   # metodo que já existe na agencia
        resultados_agencias=resultados_agencias,
        agencia_maior=agencia_maior
    )



#FUNÇÕES PARA A CONTA POUPANÇA
def aplicarRendimento(conta):
    # na poupança, aplica o rendimento se já passou 30 dias e salva só se algo mudou
    if normalizarTipo(conta.get('tipo')) != 'poupanca':
        return

    antes = conta['ultimoRendimento']   #guarda a data do último rendimento ANTES de verificar,
                                        # pra depois saber se o rendimento foi aplicado ou não
    verificarRendimento(conta)  
    #se ja passou 30 dias, essa funçao soma o rendimento ao saldo
    # e atualiza a data do ultimo rendimento pra hoje


    if conta['ultimoRendimento'] != antes:  
        salvar_dados({'clientes': clientes, 'contas': contas})
#se a data mudou, o rendimento foi aplicado, ent precisa gravar no json
#se nao mudou, naao grava nada, pra evitar salvar o arquivo à toa a cada clique


#ROTA DE DEPOSITO PRA CONTA CORRENTE E POUPANÇA
@app.route('/deposito', methods=['GET', 'POST'])
def depositar():
    #descobre quem é o cliente e qual é a conta
    #vem na URL quando abre a pagina e no formulario quando confirma
    cpf = request.values.get('cpf')
    numeroConta = request.values.get('numerodaconta')
 
    cliente = procurarCliente(clientes, cpf)
    conta = buscarContaDoCliente(cpf, numeroConta)
 
    if not cliente or not conta:                      #se tiver dados invalidos, a pessoa volta pro login
        return redirect(url_for('entrarConta'))
    
    aplicarRendimento(conta) #pra que o rendimento da conta poupança seja aplicado em deposito
 
    erro = None
    valorDigitado = ''
 
    #a pessoa clicou em "Confirmar deposito"
    if request.method == 'POST':
        valorDigitado = request.form.get('valor', '')
        valor = lerValor(valorDigitado)
 
        #escolhe a funçao de deposito de acordo com o tipo da conta
        tipo = normalizarTipo(conta.get('tipo'))
        funcaoDeposito = DEPOSITO_POR_TIPO.get(tipo)
 
        if valor is None or valor <= 0:
            erro = 'Informe um valor maior que zero'
        elif funcaoDeposito is None:
            erro = 'O depósito para este tipo de conta ainda não está disponível'
        elif funcaoDeposito(conta, valor):            # aplica as regras da conta
            salvar_dados({'clientes': clientes, 'contas': contas})
 
            #redireciona pra evitar deposito duplicado se a pagina for atualizada
            return redirect(url_for(
                'depositar',
                cpf=cpf,
                numerodaconta=numeroConta,
                sucesso=1
            ))
        else:
            erro = 'Não foi possível realizar o depósito.'
 
    #mostra a pagina (primeira visita, erro ou depósito feito com sucesso)
    sucesso = 'Depósito realizado com sucesso!' if request.args.get('sucesso') else None
 
    return render_template(
        'deposito.html',
        cliente=cliente,
        conta=conta,
        erro=erro,
        sucesso=sucesso,
        valor_digitado=valorDigitado
    )


#FUNÇÕES PRA CONTA 
    # descobre quanto a conta pode movimentar, usado na tela de saque
    # e nas mensagens de "saldo insuficiente"
def valorDisponivel(conta):
    tipo = normalizarTipo(conta.get('tipo'))
    calcular = DISPONIVEL_POR_TIPO.get(tipo)    # procura a regra do tipo da conta
 
    if calcular:
        return calcular(conta)
    return conta['saldo']    # se o tipo nao tiver regra propria, o disponível é so o saldo
 
 
def apenasDigitos(texto):
    # tira pontos, traços e espaços do cpf pra comparar só os numeros
    # ex: '123.456.789-00' vira '12345678900'
    return ''.join(c for c in str(texto or '') if c.isdigit())
 
 
def mesmoNumero(a, b):
   # compara agencia/numero da conta ignorando zeros à esquerda
    # ex '0001' e '1' contam como iguais (strip tira espaços, lstrip('0') tira os zeros)
    return str(a).strip().lstrip('0') == str(b).strip().lstrip('0')
 
 
def buscarContaDestino(agencia, numeroDestino, cpfDestino):  # procura a conta que vai RECEBER o dinheiro
    # a conta de destino só vale se agência, numero e cpf do titular baterem
    cpfLimpo = apenasDigitos(cpfDestino)
 
    for c in contas:
        if not mesmoNumero(c['agencia'], agencia):       # agencia diferente, pula
            continue
        if not mesmoNumero(c['numerodaconta'], numeroDestino):    # numero diferente, pula
            continue
 # a conta pode ter mais de um titular, ent confere a lista inteira
        titulares = [apenasDigitos(t) for t in c['clientes']]
        if cpfLimpo and cpfLimpo in titulares:
            return c
 
    return None    # nenhuma conta bateu com os tres dados



#ROTA DE SAQUE (CONTA CORRENTE E POUPANÇA)
@app.route('/saque', methods=['GET', 'POST'])
def sacar():
    # descobre quem é o cliente e qual é a conta
    # quem é o cliente e qual é a conta (URL na primeira visita, formulário ao confirmar)
    cpf = request.values.get('cpf')
    numeroConta = request.values.get('numerodaconta')
 
    cliente = procurarCliente(clientes, cpf)
    conta = buscarContaDoCliente(cpf, numeroConta)
 
    if not cliente or not conta:           # dados invalidos, volta pro login
        return redirect(url_for('entrarConta'))
    aplicarRendimento(conta)  #pra que o rendimento da conta poupança tbm seja aplicado em saque
 
    erro = None
    valorDigitado = ''    # guarda oque a pessoa digitou, pra reaparecer no campo se der algum erro
 # POST = a pessoa clicou em "Confirmar saque"
 # GET = só abriu a pagina, aí pula direto pro render_template lá embaixo
    if request.method == 'POST':
        valorDigitado = request.form.get('valor', '')    
        valor = lerValor(valorDigitado)  # transforma '1.250,50' em 1250.5 (ou None ou invalid)

        # escolhe a funçao de saque de acordo com o tipo da conta
        tipo = normalizarTipo(conta.get('tipo'))
        funcaoSaque = SAQUE_POR_TIPO.get(tipo)

 # as verificacoes vão em ordem, ent o primeiro problema encontrado vira a mensagem de erro
        if valor is None or valor <= 0:
            erro = 'Informe um valor maior que zero'

        elif funcaoSaque is None:   # tipo de conta que ainda nao tem saque implementado
            erro = 'O saque para este tipo de conta ainda não está disponível'

        elif funcaoSaque(conta, valor):               # aplica as regras da conta, True = saque feito
            salvar_dados({'clientes': clientes, 'contas': contas})  # grava o novo saldo no json
 
            # redireciona pra evitar saque duplicado se a psgina for atualizada
            return redirect(url_for(
                'sacar',
                cpf=cpf,
                numerodaconta=numeroConta,
                sucesso=1   #avisa que deu certo, pra mostrar a mensagem verde
            ))
        else:   # a funçao devolveu False, ou seja, valor acima do disponível
            erro = f'Saldo insuficiente. Você pode sacar até R$ {brl(valorDisponivel(conta))}'
 
    sucesso = 'Saque realizado com sucesso!' if request.args.get('sucesso') else None
 
    return render_template(
        'saque.html',
        cliente=cliente,
        conta=conta,
        disponivel=valorDisponivel(conta),  # valor mostrado em "Disponível para saque"
        erro=erro,
        sucesso=sucesso,
        valor_digitado=valorDigitado
    )
 



 #ROTA DE TRANFERENCIA (CONTA CORRENTE E POUPANÇA)
@app.route('/transferencia', methods=['GET', 'POST'])
def transferirDinheiro():           # cliente e conta de ORIGEM (quem está transferindo)
    cpf = request.values.get('cpf')
    numeroConta = request.values.get('numerodaconta')
 
    cliente = procurarCliente(clientes, cpf)
    conta = buscarContaDoCliente(cpf, numeroConta)
 
    if not cliente or not conta:        # dados invalidos, volta pro login
        return redirect(url_for('entrarConta'))
    aplicarRendimento(conta)  #pra que o rendimento da conta poupança tbm seja aplicado em tranferencia
 
    erro = None
    # o que que a pessoa digitou, pra não perder se der erro
    campos = {'agencia': '', 'numero_destino': '', 'cpf_destino': '', 'valor': ''}
    # POST = a pessoa clicou em "Confirmar transferência"
    if request.method == 'POST':
        campos = {
            'agencia': request.form.get('agencia', ''),
            'numero_destino': request.form.get('numero_destino', ''),
            'cpf_destino': request.form.get('cpf_destino', ''),
            'valor': request.form.get('valor', ''),
        }
 
        valor = lerValor(campos['valor'])       # procura a conta de destino com os dados digitados (None se nao existir)
        contaDestino = buscarContaDestino(
            campos['agencia'], campos['numero_destino'], campos['cpf_destino']
        )

        # escolhe a funçao de transferencia de acordo com o tipo da conta de origem
        tipo = normalizarTipo(conta.get('tipo'))
        funcaoTransferir = TRANSFERENCIA_POR_TIPO.get(tipo)
 
        if valor is None or valor <= 0:
            erro = 'Informe um valor maior que zero'
        elif funcaoTransferir is None:
            erro = 'A transferência para este tipo de conta ainda não está disponível'
        elif contaDestino is None:                     # agencia/numero/cpf nao bateram com nenhuma conta
            erro = 'Conta de destino não encontrada. Confira agência, número e CPF'
        elif contaDestino is conta:
            erro = 'Você não pode transferir para a própria conta'
        elif funcaoTransferir(conta, contaDestino, valor):   # aplica as regras da conta
            salvar_dados({'clientes': clientes, 'contas': contas})


        # redireciona pra evitar transferencia duplicada se a pagina for atualizada
            return redirect(url_for(
                'transferirDinheiro',
                cpf=cpf,
                numerodaconta=numeroConta,
                sucesso=1
            ))
        else:
            erro = f'Saldo insuficiente. Você pode transferir até R$ {brl(valorDisponivel(conta))}'
 
    sucesso = 'Transferência realizada com sucesso!' if request.args.get('sucesso') else None
 
    return render_template(
        'transferencia.html',
        cliente=cliente,
        conta=conta,
        campos=campos,
        erro=erro,
        sucesso=sucesso
    )


if __name__ == '__main__':
    app.run(debug=True)


