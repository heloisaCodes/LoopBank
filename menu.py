import json
import cliente
import conta
import agencia


# aqui ele abre o arquivo dados.json pra ler os dados que ja estão salvos
with open("dados.json", "r", encoding="utf-8") as f:
    dados = json.load(f)

# a primeira posiçao guarda os clientes
clientes = dados[0]

# a segunda guarda as contas
contas = dados[1]


print("Bem-vinda ao LoopBank!")

executando = True

while executando:
# MENU PRINCIPAL
    print("===== LOOPBANK =====")   
    print("1 - Clientes")
    print("2 - Contas")
    print("3 - Agências")
    print("4 - Relatórios")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        # abre o submenu de clientes
        
    elif opcao == "2":
        # abre o submenu de contas

    elif opcao == "3":
        # abre o de agencias

    elif opcao == "4":
        # e por fim, o de relatórios

    elif opcao == "0":
        executando = False
    else:
        print("Opção inválida!")

#SUBMENU CLIENTES
def menuClientes(clientes, contas):
    clienteMenu = True

    while clienteMenu:

        print("\n===== CLIENTES =====")
        print("1 - Cadastrar cliente")
        print("2 - Editar cliente")
        print("3 - Excluir cliente")
        print("0 - Voltar")

        opcaoCliente = input("Escolha uma opção: ")

        #CADASTRAR CLIENTE
    if opcaoCliente == "1":

        cpf = input("Digite o CPF: ")
        nome = input("Digite o nome completo: ")

        # verifica se o CPF é valido
        if cliente.validarCpf(cpf):

        # a função cadastrarCliente faz o cadastro
        # e tambem verifica se o CPF já existe
            resultado = cliente.cadastrarCliente(
                clientes, cpf, nome
                )

            if resultado:
                print("Cliente cadastrado com sucesso!")
            else:
                print("Esse CPF já está cadastrado!")

        else:
                print("CPF inválido!")
