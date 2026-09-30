from cliente import validarCpf, excluirCliente

def teste_validarCpf(cpf):
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
    print("Caso 9 passou!")

def validar_excluirCliente(cpf):
    resultado = excluirCliente()



teste_validarCpf(validarCpf)

