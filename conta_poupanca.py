from datetime import date  
import conta as modulo_conta  #apelido pra não confundir com a variavel "conta" (o dicionario)

def criarContaPoupanca(conta):
    conta['tipo'] = 'poupança' #adicionando o tipo da conta
    #e suas propiedades unicas
    conta['taxa'] = 0.005 
    conta['dataAbertura'] = '2026-09-02'
    conta['ultimoRendimento'] = '2026-10-02'

    return conta

def rendimento(conta): #calcula o rendimento
    aumento = conta['saldo'] * conta['taxa'] #calcula o aumento
    conta['saldo'] = round(conta['saldo'] + aumento, 2)   #o round pra evitar o saldo com várias casas
    #nessa parte tbm soma o aumento a conta

    return conta['saldo']

def verificarRendimento(conta):
    hoje = date.today() #pega a data de hoje graças a biblioteca
    ultimoRendimento = date.fromisoformat(conta['ultimoRendimento'])   #antes era date.isoformat, ele recebia um objeto de data, mas está sendo passado um texto
   #por isso foi trocado para date.fromisoformat, que ja transforma '2026-10-02' em data

    dias = (hoje - ultimoRendimento).days #calcula quantos dias se passaram desde o ultimo rendimento


    if dias >= 30:  #se passou um mês ou mais
        rendimento(conta)  #pega o saldo com o aumento do rendimento
        conta['ultimoRendimento'] = hoje.isoformat() # e coloca o dia atual como o ultimo rendimento

    return conta

#aqui adiciona as operaçoes
def deposito(conta, valor):
    if valor <= 0:                  # não aceita zero ou negativo
        return False
     #aqui é a mesma logica da função deposito de conta.py, pra nao repetir a regra
    conta['saldo'] = modulo_conta.deposito(conta['saldo'], valor)
    return True


def saque(conta, valor):
    # poupança nao tem limite, ela só pode sacar até o saldo
    if valor <= 0 or valor > conta['saldo']:
        return False
    conta['saldo'] = round(conta['saldo'] - valor, 2)
    return True


def transferir(conta, conta_destino, valor):
    if valor <= 0 or valor > conta['saldo']:    #mesma regra do saque,  não pode passar do saldo
        return False
    conta['saldo'] = round(conta['saldo'] - valor, 2)   # tira da conta de origem e coloca na de destino
    conta_destino['saldo'] = round(conta_destino['saldo'] + valor, 2)
    return True
