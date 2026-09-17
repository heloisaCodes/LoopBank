def criar_conta(numerodaconta, senha, cpf, agencia, saldo=0):
    clientes = []
    clientes.append(cpf)
    conta = [agencia, numerodaconta, senha, saldo, clientes]
    return conta

def cadastrarConta(contas, senha, cpf, agencia, saldo=0):
    numerodaconta = len(contas) + 1
    conta = criar_conta(numerodaconta, senha, cpf, agencia, saldo)
    contas.append(conta)
    return True
# essa função ainda vai ser mudada, porque nao levei em consideraçao caso exclua o cliente que ja possui saldo

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
    return contas

def transferir(contaOrigem, contaDestino, valor):
    if contaOrigem[3] < valor:
        return False
    else:
        contaOrigem[3] = contaOrigem[3] - valor
        contaDestino[3] = contaDestino[3] + valor
        return True

    





