agencias = {
    "0001": "Agencia 0001",
    "0002": "Agencia 0002",
    "0003": "Agencia 0003",
    "0004": "Agencia 0004",
    "0005": "Agencia 0005",
    "0006": "Agencia 0006",
    "0007": "Agencia 0007",
    "0008": "Agencia 0008",
    "0009": "Agencia 0009",
    "0010": "Agencia 0010",
    "0011": "Agencia 0011",
    "0012": "Agencia 0012",
    "0013": "Agencia 0013",
    "0014": "Agencia 0014",
    "0015": "Agencia 0015",
    "0016": "Agencia 0016",
    "0017": "Agencia 0017",
    "0018": "Agencia 0018",
    "0019": "Agencia 0019",
    "0020": "Agencia 0020",
}


def cadastrar_agencia(codigo):
    if codigo in agencias:
        return False                                    #parametros para cadastrar a agência
    elif len(codigo) == 4 and codigo.isdigit():
        agencias[codigo] = "Agencia"
        return True
    else:
        return False


def receberAgencia(clientes, cpf, agencias, contas):    #maneira de encontrar qual o valor da agencia pegando como base os 2 numeros iniciais do cpf 
    cliente = procurarCliente(clientes, cpf)
    if not cliente:
        return False

    soma = int(cpf[0]) + int(cpf[1])
    for agencia in agencias:
        if int(agencia) == soma:
            contas.append(agencia)
            return True
    return False