def procurarCliente(clientes, cpf):
    for cliente in clientes: # para cada cliente na lista clientes
        if cliente[0] == cpf: # verifica se o cpf do cliente é igual ao cpf fornecido
            return cliente # se sim, retorna o cliente

    return False

def procurarAgencia(agencias, codigo):
    for agencia in agencias: # percorre cada codigo de agencia
        if agencia == codigo: # verifica se o codigo esta em agencias
            return agencia # retorna a agencia 

    return False

def procurarPorCpf(contas, cpfbuscado):
    for conta in contas:                    #procura por conta dentro das contas 
        if cpfbuscado in conta["clientes"]: #verifica o cpf buscado dentro da conta em clientes 
            return conta                     #se achar retorna conta

    return False

def procurarPorConta(contas, numerodacontadigitado):
    for conta in contas:                                    #procura por conta dentro das contas 
        if numerodacontadigitado == conta["numerodaconta"]: #verifica o numero digitado é igual valor de numero da conta 
            return conta 
            
    return False
