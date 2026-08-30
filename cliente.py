def cadastrarCliente():
    nome = input('Nome Completo: ')
    cpf = input('Cpf: ')
    cliente = (nome, cpf)
    
    return cliente

def validarCpf(cpf):
    if len(cpf) != 11 or cpf[0] * 11:
        return False
    else:
        return True
    


cliente = cadastrarCliente()
cpf = cliente[1]
if validarCpf(cpf):
    print('CPF Válido!')
else:
    print('CPF Inválido!')
