#procurarCliente
def procurarCliente(clientes, cpf):
    for cliente in clientes: #para cada cliente na lista clientes
        if cliente[0] == cpf: #verifica se o cpf do cliente é igual ao cpf fornecido
            return cliente #se sim, retrorna o cliente

    return False

def procurarAgencia(agencias, codigo):
    for agencia in agencias: #pecorre cada codigo de agencia
        if agencia == codigo: #verifica se o codigo esta em agencias
            return agencia #retorna a agencia 

    return False
