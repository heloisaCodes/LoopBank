from conta import listarContas

def montanteBanco(contas):
    montanteSaldo = 0
    contas = listarContas(contas) #lista de todas as contas
    for conta in contas:
        montanteSaldo += conta[3] #pega o saldo de cada conta e vai somando

    return montanteSaldo #o dinheiro total de todas as contas

def montanteAgencia(contas, agencias): #pega a lista agencias
    contas = listarContas(contas) #lista de todas as contas
    resultado = []

    for agencia in agencias: # para cada agencia da lista agencias
        contadorAgencia = 0
        for conta in contas: #ler as contas
            if contas[1] == agencia: #se a agencia da conta atual for a mesma da agencia lida no momento
                quantClientes = len(conta[4]) #pega a quatidade de clientes vinculados aquela conta
                contadorAgencia += quantClientes #soma isso a quantidade de clientes da agencia
        # faz isso para todas as contas
        resultado.append((agencia, contadorAgencia)) #depois salva a quantidade aquela agencia, e vai para a proxima

    return resultado 



