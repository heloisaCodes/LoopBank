import cliente

def inicio():
    print("Bem-vinda ao LoopBank!")

    #cliente = cliente.cadastrarCliente

cpf = input("Digite seu CPF:")
if cliente.validarCpf:
 print('CPF Válido!')
else:
    print('CPF Inválido!')

inicio()