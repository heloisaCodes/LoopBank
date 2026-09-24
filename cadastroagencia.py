agencia = [
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
    #essa parte avalia o tamanho do codigo e se os caracteres digitados são digitos

def receberAgencia(clientes, cpf, agencias, contas):
    cliente = procurarCliente(clientes, cpf)

    soma = int(cpf[0]) + int(cpf[1])
    for agencia in agencias:
        if int(agencia) == soma:
            contas[]
        else:
            return False
    #falta terminar