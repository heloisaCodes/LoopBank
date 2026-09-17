import cliente
import conta

print("Bem-vinda ao LoopBank!")
nome = input("Nome completo:")
cpf = input("CPF:")

if cliente.validarCpf(cpf):
    print('CPF Válido!')
    cliente.cadastrarCliente(nome, cpf)
else:
    print('CPF Inválido!')


numerodaconta = input("Digite o número da conta:")
senha = input("Digite sua senha:")
minha_conta = conta.criar_conta(numerodaconta, senha)

print("Sua conta foi criada com sucesso!")

agencia = int(input("Digite sua agência:"))
senha_login = input("Digite sua senha:")

resultado = conta.autenticar(minha_conta, agencia, senha_login)
if resultado:
    valor_deposito = float(input("Quanto deseja depositar?"))
    minha_conta["saldo"] = conta.deposito(
    minha_conta["saldo"], valor_deposito
     )

    print("Seu saldo atual é:", minha_conta["saldo"])

    valor_saque = float(input("Quanto deseja sacar?"))
    minha_conta["saldo"] = conta.saque(
        minha_conta["saldo"], valor_saque
        )

    print("Seu saldo atual é:", minha_conta["saldo"])
else:
    print("ERRO!")



















    