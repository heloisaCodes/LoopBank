import json
import submenuConta
import submenuCliente


# aqui ele abre o arquivo dados.json pra ler os dados que ja estão salvos
with open("dados.json", "r", encoding="utf-8") as f:
    dados = json.load(f)

# a primeira posiçao guarda os clientes
clientes = dados[0]

# a segunda guarda as contas
contas = dados[1]


print("Bem-vinda ao LoopBank!")

executando = True
def menuprincipal ():
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
        #abre o submenu de clientes
            submenuCliente.menuClientes(clientes,contas)
        
        elif opcao == "2":
        # abre o submenu de contas
            submenuConta.menuContas(contas)

        elif opcao == "3":
        # abre o de agencias

        elif opcao == "4":
        # e por fim, o de relatórios
            
        elif opcao == "0":
            executando = False
            # voltar pra parte incicial, fechar a aba "menu"

