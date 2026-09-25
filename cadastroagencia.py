agencias = [
    "0001", "0002", "0003", "0004", "0005",
    "0006", "0007", "0008", "0009", "0010",
    "0011", "0012", "0013", "0014", "0015"
]

def cadastrar_agencia(codigo):
    if codigo in agencias:
        return False
    elif len(codigo) == 4 and codigo.isdigit():
        agencias.append(codigo)
        return True
    else:
        return False
        # verifica se o codigo da agência digitado está nos parâmetros

def receberAgencia(clientes, cpf, agencias, contas):
    cliente = procurarCliente(clientes, cpf)
    if not cliente:
        return False

    soma = int(cpf[0]) + int(cpf[1])

    for agencia in agencias:
        if int(agencia) == soma:
            contas.append(agencia)
            return True

    return False