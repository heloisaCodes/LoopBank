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