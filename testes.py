from cliente import validarCpf, excluirCliente

# TESTE 1: VALIDAÇÃO DO CPF
def teste_validarCpf(cpf):
    resultado = validarCpf('17822790080') #cpf correto, seguindo todas as regras
    assert resultado == True

    resultado =  validarCpf('17822790070') #cpf com o primeiro digito verificador errado, cpf invalido
    assert resultado == False 

    resultado = validarCpf('17822790083') #cpf com o segundo digito verificador errado, cpf invalido
    assert resultado == False

    resultado = validarCpf('17822790072') #cpf com os dois digitos verificadores errado
    assert resultado == False 

    resultado = validarCpf('1782279007') #cpf com menos de 11 digitos
    assert resultado == False

    resultado = validarCpf('178227900700') #cpf com mais de 11 digitos
    assert resultado == False

    resultado = validarCpf('18-27!0$7.0') #cpf com caracteres nao numericos
    assert resultado == False

    resultado = validarCpf('           ') #cpf vazio
    assert resultado == False

    resultado = validarCpf('00000000000') #cpf com todos os digitos iguais
    assert resultado == False

#TESTE 2: TESTA EXCLUIR CLIENTE

def teste_excluirCliente_semsaldo(): #cliente existe e não tem saldo em nenhuma conta

    #começo fornecendo os dados que a função precisa para funcionar
    cliente = {
                'cpf': '17822790080',  #dados do cliente
                 'nome':'Heloísa'
                 }    

    cliente2 = {
                'cpf': '19040765057',  #dados do cliente
                 'nome':'Eduarda'
                 }    
    
    clientes = [cliente, cliente2]

    conta = {
                'agencia':'0002',
                'numero da conta': '102',
                'senha': '2587',
                'saldo': 0,                     #conta conjunta
                'clientes': [cliente, cliente2]
                }  
    
    contas = [conta]

    resultado = excluirCliente('17822790080', clientes, contas) #chamo a função 
    assert resultado == True #vendo se o resultado é igual ao esperado
    assert cliente not in clientes #verificando se o cliente foi excluido dos clientes
 

def teste_excluirCliente_comsaldo(): #cliente existe e possui no minimo 1 conta com saldo
    cliente = {
            'cpf': '17822790080',  #dados do cliente
             'nome':'Heloísa'
             }    
    clientes = [cliente]

    conta = {
            'agencia':'0001',
            'numero da conta': '101',
            'senha': '1234',          # primeira conta do cliente
            'saldo': 500,
            'clientes': [cliente]
            } 
    
    conta2 = {
            'agencia':'0002',
            'numero da conta': '102',
            'senha': '2587',          # segunda conta do cliente
            'saldo': 0,
            'clientes': [cliente]
            } 
    contas = [conta, conta2]

    resultado = excluirCliente('17822790080', clientes, contas)
    assert resultado == False  #Espera que o cliente nao tenha sido excluido
    assert cliente in clientes #logo cliente não foi excluido, ele ainda está cadastrado no banco


def teste_excluirCliente_errado():
    cliente = {
        'cpf': '17822790080',  #dados do cliente
         'nome':'Heloísa'
         }  
    clientes = [cliente] #lista clientes

    conta = {
        'agencia':'0002',
        'numero da conta': '102',
        'senha': '2587',          #conta do cliente
        'saldo': 0,
        'clientes': [cliente]
        } 
    contas = [conta]

    resultado = excluirCliente('19040765057', clientes, contas) #excluir um cliente que não existe
    assert resultado == False #não da
    assert cliente in clientes #cliente não foi excluido




teste_validarCpf(validarCpf)
teste_excluirCliente_semsaldo()
teste_excluirCliente_comsaldo()
teste_excluirCliente_errado()