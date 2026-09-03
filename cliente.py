def cadastrarCliente():
    cliente = (nome, cpf)
    
    return cliente

def validarCpf(cpf):
    if len(cpf) != 11 or cpf[0] * 11:
        return False
    else:
        return True
    


cliente = cadastrarCliente()
cpf = cliente[1]