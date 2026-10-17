#TESTE CADASTRO
from conta import criar_conta, cadastrarConta, autenticar

contas_teste = []

resultado = cadastrarConta(contas_teste, "1234", "11122233344", 1234)

print("Cadastro:", resultado)
print("Contas:", contas_teste)


#TESTE DEPOSITO E SAQUE
from conta import deposito, saque

saldo = 100

print("Depósito válido:", deposito(saldo, 50))
print("Depósito zero:", deposito(saldo, 0))

print("Saque válido:", saque(saldo, 30))
print("Saque maior que o saldo:", saque(saldo, 150))


#TESTE TRANSFERIR
from conta import transferir

conta_origem = {"saldo": 200}
conta_destino = {"saldo": 50}

resultado = transferir(conta_origem, conta_destino, 80)

print("Transferência:", resultado)
print("Saldo da origem:", conta_origem["saldo"])
print("Saldo do destino:", conta_destino["saldo"])


#TESTE DE AUTENTICAR
from conta import autenticar

conta_teste = {
    "senha": "1234"
}

print("Senha correta:", autenticar(conta_teste, "1234"))
print("Senha incorreta:", autenticar(conta_teste, "9999"))