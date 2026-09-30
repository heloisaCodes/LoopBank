def criar_conta(numerodaconta, senha, cpf, agencia, saldo=0):
    clientes = [] #clientes precisa ser lista
    clientes.append(cpf)

    # conta agora vira dicionário
    conta = {
            "agencia": agencia,
            "numerodaconta": numerodaconta,
            "senha": senha,
            "saldo": saldo,
            "clientes": clientes
               }
            
    return conta


def cadastrarConta(contas, senha, cpf, agencia, saldo=0):  # ou seja, pega a conta e coloca ela na lista geral de contas
    # numero da conta é gerada na hora
    numerodaconta = len(contas) + 1  # aqui serve como um contador 
    conta = criar_conta(numerodaconta, senha, cpf, agencia, saldo=0)
    contas.append(conta)
    return True  # pra saber se o cadastro deu certo

    

# aqui vamos ver se a senha e a agencia digitadas estão corretas
def autenticar(conta, agenciadigitada, senhadigitada):
    if conta["agencia"] != agenciadigitada:  
        return False
    elif conta["senha"] != senhadigitada:   
        return False
    else:                          # ou seja, se nenhuma delas estiver errada, vai ser retornado True
        return True   

    
# pra nao permitir sacar mais dinheiro do que o que tiver
def saque(saldoatual, valordosaque):    
    if saldoatual < valordosaque:        # se o saldo for menor que  o valor do saque
        return saldoatual                # ent retorna o saldo atual
    else:
        return saldoatual - valordosaque  # caso nao, retorna o saldo MENOS o valor do saque

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
    if contaOrigem["saldo"] < valor:
        return False

    # como a conta agora é de dicionarios, ent calculamos apenas os novos saldos
    novoSaldoOrigem = contaOrigem["saldo"] - valor
    novoSaldoDestino = contaDestino["saldo"] + valor

    # agora esses novos valores voltam pro dicionario
    contaOrigem["saldo"] = novoSaldoOrigem
    contaDestino["saldo"] = novoSaldoDestino
    # retorna esses valores
    return contaOrigem, contaDestino



