def criar_conta(numerodaconta, senha, cpf, agencia, saldo=0):
    clientes = []
    clientes.append(cpf)

    # conta agora vira TUPLA
    conta = (agencia, numerodaconta, senha, saldo, clientes)
    return conta


def cadastrarConta(contas, senha, cpf, agencia, saldo=0):
    # numero da conta é gerada na hora
    numerodaconta = len(contas) + 1

    # aqui vai ser criada a conta
    conta = criar_conta(numerodaconta, senha, cpf, agencia, saldo)
    contas.append(conta)
    return True


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

    # Como a conta é uma tupla, ent calcula os novos saldos e depois deixa tudo atualizad
    novoSaldoOrigem = contaOrigem[3] - valor
    novoSaldoDestino = contaDestino[3] + valor

    novaContaOrigem = (
        contaOrigem[0],
        contaOrigem[1],
        contaOrigem[2],
        novoSaldoOrigem,
        contaOrigem[4]
    )

    novaContaDestino = (
        contaDestino[0],
        contaDestino[1],
        contaDestino[2],
        novoSaldoDestino,
        contaDestino[4]
    )

    return novaContaOrigem, novaContaDestino





