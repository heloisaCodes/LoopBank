import cliente
import conta

nome = input("Nome completo:")
cpf = input("CPF:")
def inicio():
    print("Bem-vinda ao LoopBank!")
    if cliente.validarCpf(cpf):
        print('CPF Válido!')
        cliente.cadastrarCliente(nome, cpf)
    else:
        print('CPF Inválido!')
inicio()

numerodaconta = input("Digite o número da conta:")
senha = input("Digite sua senha:")
minha_conta = conta.criar_conta(numerodaconta, senha)
print("Sua conta foi criada com sucesso!")

agencia = int(input("Digite sua agência:"))
senha_login = input("Digite sua senha:")

def login(minha_conta, agencia, senha_login):
    resultado = conta.autenticar(minha_conta, agencia, senha_login)
    if resultado == False:
        print("ERRO")
    else:
        print("Quanto deseja depositar?")
        valor_deposito = float(input())
        minha_conta["saldo"] = conta.deposito(minha_conta["saldo"], valor_deposito)
        print("Depósito realizado com sucesso")

        print("Seu saldo atual é:", minha_conta["saldo"])
        print("Quanto deseja sacar?")
        valor_saque = float(input())
        
        minha_conta["saldo"] = conta.saque(minha_conta["saldo"],valor_saque)
        print("Saque realizado com sucesso!")
        print("Seu saldo atual é:", minha_conta["saldo"])


login(minha_conta, agencia, senha_login)
    