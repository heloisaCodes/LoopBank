from cliente import validarCpf, excluirCliente

""" def teste_validarCpf(cpf):
    resultado = validarCpf('17822790080') #cpf correto, seguindo todas as regras
    assert resultado == True
    print("Caso 1 passou!")

    resultado =  validarCpf('17822790070') #cpf com o primeiro digito verificador errado, cpf invalido
    assert resultado == False 
    print("Caso 2 passou!")

    resultado = validarCpf('17822790083') #cpf com o segundo digito verificador errado, cpf invalido
    assert resultado == False
    print("Caso 3 passou!")

    resultado = validarCpf('178.227.900-72') #cpf com os dois digitos verificadores errado
    assert resultado == False 
    print("Caso 4 passou!")

    resultado = validarCpf('1782279007') #cpf com menos de 11 digitos
    assert resultado == False
    print("Caso 5 passou!")

    resultado = validarCpf('178227900700') #cpf com mais de 12 digitos
    assert resultado == False
    print("Caso 6 passou!")

    resultado = validarCpf('178.227.900-70') #cpf com caracteres nao numericos
    assert resultado == False
    print("Caso 7 passou!")

    resultado = validarCpf('           ') #cpf vazio
    assert resultado == False
    print("Caso 8 passou!")

    resultado = validarCpf('00000000000') #cpf com todos os digitos iguais
    assert resultado == False
    print("Caso 9 passou!") """

""" def teste_excluirCliente_semsaldo(): #cliente existe e não tem saldo em nenhuma conta

    #começo fornecendo os dados que a função precisa para funcionar
    cliente = ('17822790080', 'Heloísa')  
    cliente2 = ('19040765057', 'Eduarda')
    clientes = [cliente, cliente2]

    conta = ['0001', 101, '1234', 0, [cliente, cliente2]] #testando com conta conjunta
    contas = [conta]

    resultado = excluirCliente('17822790080', clientes, contas) #chamo a função 
    assert resultado == True #vendo se o resultado é igual ao esperado
    assert cliente not in clientes #verificando se o cliente foi excluido dos clientes
    print(f''' {clientes}
{contas}''') """

def teste_excluirCliente_comsaldo(): #cliente existe e possui no minimo 1 conta com saldo
    cliente = ('17822790080', 'Heloísa')  
    clientes = [cliente]

    contaSemSaldo = ['0001', 101, '1234', 500, [cliente]] 
    contaComSaldo = ['0002', 102, '2587', 0, [cliente] ] #cliente posssui duas contas
    contas = [contaSemSaldo, contaComSaldo]

    resultado = excluirCliente('17822790080', clientes, contas)
    assert resultado == True #Nesse tiramos o cliente da conta sem saldo e deixamos ele na com saldo
    assert cliente not in contaSemSaldo
    assert cliente in contaComSaldo 
    assert cliente in clientes #logo cliente não foi excluido, ele ainda está cadastrado no banco
    print(f''' {clientes}
{conta}''')


teste_excluirCliente_comsaldo()
#teste_excluirCliente_semsaldo()



#teste_validarCpf(validarCpf)

