from procurar import procurarCliente, procurarConta

def cadastrarCliente(clientes, cpf, nome):
    if procurarCliente(clientes, cpf): # Procurou o cliente e retornou o cliente (o cliente já está cadastrado)
        return False                   # Então não precisa continuar
    else:                              # Cadastro do cliente novo
        cliente = (cpf, nome)
        clientes.append(cliente)       # Adicona a lista clientes
        
        return cliente 


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
    cliente = procurarCliente(clientes, cpf) #cliente retornado

    if cliente: # Se o cliente existe

        for i in range(clientes):            #percorre a lista clientes
            if clientes[i] == cliente:       #se o cliente atual da lista é igual ao cliente procurado
                cliente[i] = (cpf, novoNome) #substitui a tupla antiga pela nova com o nome editado
        
        return True
    
    else:
        return False
    
def excluirCliente(cpf, clientes, contas):
    cliente = procurarCliente(clientes, cpf)    #retorna o cliente
    contasCliente = procurarConta(contas, cpf)  #retorna as contas
    if cliente:
        contasSemSaldo = []
        contasComSaldo = 0

        for conta in contasCliente:    #verifica cada conta do cliente
            if conta[3] != 0:              #se a conta tiver saldo
                contasComSaldo += 1
            else:
                contasSemSaldo.append(conta)    #adiciona a tupla a lista

        if contasComSaldo == 0:    #nenhuma conta tem saldo
            clientes.remove(cliente)     #exclui o cliente
            return True
        
        else:                             #alguma conta tem saldo
            for conta in contasSemSaldo: 
                conta.remove(conta[4])    #tira o cliente da conta

            return True

    else:
        return False

def listarClientes(clientes):
    return clientes



