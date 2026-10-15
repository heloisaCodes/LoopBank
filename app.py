import json
import os
from flask import Flask, render_template, request, redirect, url_for
from procurar import procurarCliente, procurarPorCpf
from conta import autenticar, cadastrarConta
from cliente import cadastrarCliente
from agencia import receberAgencia, agencias 

app = Flask(__name__) #cria a aplicação web

# Nome do arquivo onde os dados serão salvos
ARQUIVO_DADOS = 'dados.json'

# Função para carregar clientes e contas a partir de um arquivo JSON
def carregar_dados():
    """Lê a lista de clientes e contas salva no arquivo JSON."""
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {"clientes" : [], "contas" : []}

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
    cliente = cadastrarCliente(clientes, cpf, nome) #procura o cliente pelo cpf dado

    if not cliente: #se o cliente existe retorna falso, então não falso = verdadeiro
        clienteCadastrado = procurarCliente(clientes, cpf)
        return redirect(url_for(
            'entrarConta',
              cpf=cpf,                                #caso do cliente já cadastrado = vai para a pagina de login 
              mensagem='Este CPF já está cadastrado.',
              nome=clienteCadastrado['nome']
              )) 
    
    agencia = receberAgencia(clientes, cpf, agencias)
    contaCliente = cadastrarConta(contas, senha, cpf, agencia)
    
    if contaCliente:  #cadastro bem sucedido
        salvar_dados({
            'clientes': clientes,   #salva os dados
            'contas': contas
            })
        
        return redirect(url_for('area_cliente'))  #vai para a area do cliente, entra no banco



@app.route('/login', methods=['GET', 'POST']) #ou faz o login
def entrarconta():
    if request.method == 'GET':  #mostra a pagina
        return render_template('login.html')

    cpf = request.form.get('cpf')                  #pega os dados dos clientes
    senhadigitada = request.form.get('senha')

    cliente = procurarCliente(clientes, cpf)  #cliente com respectivo codigo

    if cliente:            #cliente já está cadastrado
        contasCorrespondentes = []

        for conta in contas:
            if cpf in conta['clientes']:  #verifica todas as contas do cliente
                verificasenha = autenticar(conta, senhadigitada) #autenticar está fazendo a comparação

                if verificasenha:
                    contasCorrespondentes.append(conta)

        if len(contasCorrespondentes) == 1:  #a senha pertence a apenas 1 conta
            return render_template(
                'cliente.html',
                conta=contasCorrespondentes[0] #entra na conta especifica
            )

        elif len(contasCorrespondentes) > 1: #mais de 1 conta possui a mesma senha ps: em conta.py nas funções referentes não tem nenhuma restrição de senha
            return render_template(
                'selecionar_conta.html',      #mostra a lista de contas do cliente (com a mesma senha)
                contas=contasCorrespondentes
            )

        else:  #senha errada, tenta dnv
            return render_template(
                'login.html',
                mensagem='Senha incorreta.'
            )

    else:  #cliente não está cadastrado
        return redirect(url_for('cadastroCliente')) #vai para cadastro



if __name__ == '__main__':
    app.run(debug=True)