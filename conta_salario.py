import conta
# a ideia é fazer uma conta salario ligada a uma empresa especifica, uma relaçao mais simples entre o cliente e a empresa


def identificar (documento): # a ideia é permitir apenas que empresas depositem o dinheiro
    if len(documento) == 11:    # o cpf tem 11 numeros , enquanto o cnpj tem 14, entaoo eu peço pra ele retornar o cnpj
        return "CPF"
    elif len(documento) == 14:
        return "CNPJ"
    else:
        return False

cnpj = []

def validarCNPJ(cnpj):  # ver se de fato é um cnpj valido
    # primeiro verifica se todos os caracteres sao numeros
    for caractere in cnpj:
        if caractere < "0" or caractere > "9":
            return False

    # nao permite que todos os numeros sejam iguais
    if cnpj == cnpj[0] * 14:
        return False

    # aqui temos os pesos pra calculo
    # do primeiro dígito verificador do CNPJ
    peso1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    soma = 0

    for i in range(12):                  # percorre os 12 primeiros caracteres
        soma += int(cnpj[i]) * peso1[i]  # o cnpj[i] pega o numero naquela posicao

    resto = soma % 11  # pega o resto da divisao da soma por 11
    if resto < 2:    # qual deveria ser o primeiro digito verificador        
        dig1 = 0
    else:
        dig1 = 11 - resto

    if dig1 != int(cnpj[12]):
        return False
    # o primeiro digito verificador calculado
    # precisa ser igual ao 13° n° do CNPJ, ent cnpj[12] = posição 13
    # se forem diferentes, o CNPJ não passa

     # outro peso usado pra calcular o segundo digito
    peso2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    soma = 0
    # aqui usamos os 13 primeiros numeros e segue a msm ideia
    for i in range(13):
        soma += int(cnpj[i]) * peso2[i]

    resto = soma % 11
    if resto < 2:
        dig2 = 0
    else:
        dig2 = 11 - resto

    # ver se o 2° digito calculado la em cima é igual ao ultimo numero do CNPJ
    if dig2 != int(cnpj[13]):  # cnpj[13] = posiçao 14 ja que começa do 0
        return False

    return True

        
 # se for CNPJ, cria a conta 
def criarContaSalario (clientes, empresa, salario, saldo=0):   
    conta = {
        "clientes": [clientes],
        "tipo": "salario",
        "empresa": empresa,
        "salário": salario,
        "saldo": saldo
                }
    return conta

    
    # se cliente receber algo, pode pedir portabilidade, que seria a mesma logica do que ja foi feito em conta
def portabilidade(conta_salario, conta_destino, valor):   # pega o valor da conta salario e pode transferir pra outra conta
    resultado = conta.transferir(
        conta_salario,
        conta_destino,
        valor
    )

    return resultado
# serviria tanto pra transferir pra outro banco ou pra mesma conta (conta corrente)
    
