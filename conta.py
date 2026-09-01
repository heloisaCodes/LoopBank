
def saque(saldoatual):
    valordosaque = int(input("Digite o valor do saque: "))
    
    if saldoatual < valordosaque: 
        print("Saldo Insuficiente")
        return saldoatual
    else:
        novosaldo = saldoatual - valordosaque
        print(f"Saque bem sucedido! Saldo atual: R${novosaldo}")
        return novosaldo


def deposito(saldoatual):
    valordodeposito = int(input("Digite o valor do deposito: "))

    if valordodeposito <= 0 :
       print("valor invalido")
       return saldoatual 
    else:
        novosaldo = saldoatual + valordodeposito
        print(f"Deposito bem sucedido! Saldo atual : R${novosaldo}")
        return novosaldo


saldo = 100
saldo = saque(saldo)
saldo = deposito(saldo)