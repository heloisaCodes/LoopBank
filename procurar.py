def procurarCliente(clientes, cpf):
    for cliente in clientes: # para cada cliente na lista clientes
        if cliente['cpf'] == cpf: # verifica se o cpf do cliente é igual ao cpf fornecido
            return cliente # se sim, retorna o cliente

    return False

def procurarAgencia(agencias, codigo):
    for agencia in agencias: # percorre cada codigo de agencia
        if agencia == codigo: # verifica se o codigo esta em agencias
            return agencia # retorna a agencia 

    return False

def procurarPorCpf(contas, cpf):
    contasCliente = [] #cria uma lista vazia para armazenar as contas do cliente
    for conta in contas:                    #procura por conta dentro das contas 
        if cpf in conta['clientes']: #verifica o cpf buscado dentro da conta em clientes 
            contasCliente.append(conta) #adiciona a conta à lista

    return contasCliente

def procurarPorConta(contas, numerodacontadigitado):
    for conta in contas:                                    #procura por conta dentro das contas 
        if numerodacontadigitado == conta["numerodaconta"]: #verifica o numero digitado é igual valor de numero da conta 
            return conta 
            
    return False
