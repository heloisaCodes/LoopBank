def criar_conta(numerodaconta, senha, agencia=1234, saldo=100):
    return {
        "agencia": agencia,
        "numerodaconta": numerodaconta,
        "senha": senha,
        "saldo": saldo
    }

def autenticar(conta, agenciadigitada, senhadigitada):
    if conta["agencia"] != agenciadigitada:
        return False
    elif conta["senha"] != senhadigitada:
        return False
    else:
        return True

def saque(saldoatual, valordosaque):
    if saldoatual < valordosaque: 
        return saldoatual
    else:
        return saldoatual - valordosaque

def deposito(saldoatual, valordodeposito):
    if valordodeposito <= 0:
        return saldoatual 
    else:
        return saldoatual + valordodeposito