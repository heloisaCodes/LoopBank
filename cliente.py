from procurar import procurarCliente


def cadastrarCliente(clientes, nome, cpf):
    if procurarCliente(clientes, cpf): # Procurou o cliente e retornou o cliente (o cliente já está cadastrado)
        return False # Então não precisa continuar
    else: # Cadastro do cliente novo
        cliente = []
        cliente.append(nome)
        cliente.append(cpf)
        clientes.append(cliente) # Adicona a lista clientes
        
        return True


def validarCpf(cpf):
    # Verifica se o cpf tem 11 caracteres ou se possui todos os dígitos iguais
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False
    # Acumuladores inicializados
    soma1 = 0
    soma2 = 0

    # Verificação do penúltimo dígito
    for i in range(0, 9):
        soma1 += int(cpf[i]) * (10 - i)

    resto1 = soma1 % 11
    if resto1 == 0 or resto1 == 1:
        digito1 = 0
    else:
        digito1 = 11 - resto1

    # Verificação do último dígito
    for i in range(0, 10):
        soma2 += int(cpf[i]) * (11 - i)

    resto2 = soma2 % 11
    if resto2 == 0 or resto2 == 1:
        digito2 = 0
    else:
        digito2 = 11 - resto2

    return digito1 == int(cpf[9]) and digito2 == int(cpf[10])

def editarCliente(clientes, cpf, novoNome):
    cliente = procurarCliente(clientes, cpf) # Associando a lista cliente retornada a variavel cliente
    if cliente: # Se o cliente existe
        cliente[0] = novoNome #Substitui o nome
        return True
    else:
        return False
    
#def excluirCliente():
