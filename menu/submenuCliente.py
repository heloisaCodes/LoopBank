import cliente
def menuClientes(clientes, contas):
    # vê se o submenu de clientes continua aberto ou se deve voltar pra o menu principal
    clienteMenu = True

    while clienteMenu:

        print("\n===== CLIENTES =====")
        print("1 - Cadastrar cliente")
        print("2 - Editar cliente")
        print("3 - Excluir cliente")
        print("4 - Listar clientes")
        print("0 - Voltar")

        opcaoCliente = input("Escolha uma opção: ")

         # CADASTRAR CLIENTE
        if opcaoCliente == "1":
            # primeiro pegamos os dados do cliente
            cpf = input("Digite o CPF: ")
            nome = input("Digite seu nome completo: ")

            # antes de cadastrar, verificamos se o CPF é valido
            if cliente.validarCpf(cpf):
                resultado = cliente.cadastrarCliente(         # ou seja, se tiver tudo certo, adiciona o cliente na lista
                    clientes,
                    cpf,
                    nome
                )

                if resultado:
                    print("Cliente cadastrado com sucesso!")
                else:
                    print("Esse CPF já está cadastrado!")

            else:
                print("CPF inválido")


         # EXCLUIR CLIENTE
        elif opcaoCliente == "3":

            # pedimos o CPF do cliente que vai ser excluido
            cpf = input("Digite o CPF: ")

            # A função excluirCliente verifica se o cliente
            # existe e se pode ser excluído.
            resultado = cliente.excluirCliente(
                cpf,
                clientes,
                contas
            )

            if resultado:
                print("Cliente excluído com sucesso!")
            else:
                print("Não foi possível excluir o cliente")



         # LISTAR CLIENTES
        elif opcaoCliente == "4":

            # pegamos a lista de clientes atraves da funçao que tá no cliente
            listaClientes = cliente.listarClientes(clientes)

            # vê se existe algum cliente cadastrado
            if len(listaClientes) == 0:
                print("Nenhum cliente cadastrado")

            else:
                print("\n===== LISTA DE CLIENTES =====")
                # como nessa etapa 2, cada cliente era uma tupla, entao seria (cpf, nome)
                for pessoa in listaClientes:
                    print("CPF:", pessoa[0])
                    print("Nome:", pessoa[1])

         # VOLTAR
        elif opcaoCliente == "0":
            # se mudar pra False, o while termina, e ai voltamos pra o menu principal
            clienteMenu = False
               
