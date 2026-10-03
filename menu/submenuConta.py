import conta

# funçao responsavel pelo submenu de contas
def menuContas(contas):
    executando = True

    while executando:
        print("\n===== CONTAS =====")
        print("1 - Cadastrar conta")
        print("2 - Listar contas")
        print("3 - Consultar saldo")
        print("4 - Sacar")
        print("5 - Depositar")
        print("6 - Transferir")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        # aqui cadastra uma nova conta
        if opcao == "1":
            cpf = input("Digite o CPF: ")
            senha = input("Digite a senha: ")
            agencia = input("Digite a agência: ")

            # a funçao cadastrarConta ja cria o numero da conta
            resultado = conta.cadastrarConta(
                contas,
                senha,
                cpf,
                agencia
            )

            if resultado:
                print("Conta cadastrada com sucesso!")

        # pra listar todas as contas cadastradas
        elif opcao == "2":
            contasCadastradas = conta.listarContas(contas)

            # ver se existe alguma conta
            if len(contasCadastradas) == 0:
                print("Nenhuma conta cadastrada")
            else:
                for contaAtual in contasCadastradas:
                    print("Agência:", contaAtual[0])
                    print("Número da conta:", contaAtual[1])
                    print("Saldo:", contaAtual[3])
                    print("Clientes:", contaAtual[4])

        # por fim, pra ele voltar pro menu principal
        elif opcao == "0":
            executando = False  # a msm logica em todas
        