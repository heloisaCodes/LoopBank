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
    contas.append(conta)  #adiciona conta na lista de contas
    return True


def autenticar(conta, agenciadigitada, senhadigitada):
    if conta[0] != agenciadigitada:  # porque conta[0] é agencia
        return False
    elif conta[2] != senhadigitada:   # conta[2] é senha
        return False
    else:
        return True
    
# pra nao permitir sacar mais dinheiro do que o que tiver
def saque(saldoatual, valordosaque):    
    if saldoatual < valordosaque:
        return saldoatual
    else:
        return saldoatual - valordosaque

# nao permite depósito de valor 0 ou negativo 
def deposito(saldoatual, valordodeposito):
    if valordodeposito <= 0:
        return saldoatual
    else:
        return saldoatual + valordodeposito


def listarContas(contas): 
    # apenas retorna a lista de contas
    return contas


def transferir(contaOrigem, contaDestino, valor):
    # ver se existe saldo suficiente
    if contaOrigem[3] < valor:
        return False

    # como a conta é uma tupla, ent calcula os novos saldos e depois deixa tudo atualizado
    novoSaldoOrigem = contaOrigem[3] - valor
    novoSaldoDestino = contaDestino[3] + valor

# novas tuplas com os saldos atualizados
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
    # retorna as duas contas atualizadas




