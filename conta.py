def criar_conta(numerodaconta, senha, cpf, agencia=1234, saldo=0):
    clientes = []
    clientes.append(cpf)
    conta = [agencia, numerodaconta, senha, saldo, clientes]
    return conta

def autenticar(conta, agenciadigitada, senhadigitada):
    if conta[0] != agenciadigitada:
        return False
    elif conta[2] != senhadigitada:
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

def listarContas(contas):
    listaContas = []
    for conta in contas:
        listaContas.append(conta)
    return listaContas

def transferir(contaOrigem, contaDestino, valor):
    if contaOrigem[3] < valor:
        return False
    else:
        contaOrigem[3] = contaOrigem[3] - valor
        contaDestino[3] = contaDestino[3] + valor
        return True

    





