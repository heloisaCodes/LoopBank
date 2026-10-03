from datetime import date
import conta #pega as caracteristicas basicas de uma conta, que de todos os tipos tem

def criarContaPoupanca(conta):
    conta['tipo'] = 'poupança' #adicionando o tipo da conta
    #e suas propiedades unicas
    conta['taxa'] = 0.005 
    conta['dataAbertura'] = '2026-09-02'
    conta['ultimoRendimneto'] = '2026-10-02'

    return conta

def rendimento(conta): #calcula o rendimento
    aumento = conta['saldo'] * conta['taxa'] #calcula o aumento
    conta['saldo'] += aumento #soma o aumento a conta

    return conta['saldo']

def verificarRendimento(conta):
    hoje = date.today() #pega a data de hoje graças a biblioteca
    ultimoRendimento = date.isoformat(conta['ultimoRendimento']) #formata a data ao padrao
    dias = (hoje - ultimoRendimento).days #calcula quantos dias se passaram desde o ultimo rendimento


    if dias >= 30: #se passou um mês ou mais
        rendimento(conta) #pega o saldo com o aumento do rendimento
        conta['ultimoRendimento'] = hoje.isoformat()# e coloca o dia atual como o ultimo rendimento

    return conta
    
