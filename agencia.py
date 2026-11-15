from functools import reduce

class Agencia:

    def __init__(self, numero, clientes, contas):
        self.numero = numero
        self.clientes = clientes
        self.contas = contas

    def montante(self): #somar todos os saldos, como temo apenas 1 agência correponde há o saldo de todas as contas da agencia/banco
        montante = 0
        for conta in self.contas: #soma o saldo de cada conta
            montante += conta.saldo

        return montante

    def maiorSaldo(self):
        saldos = map(lambda conta: conta.saldo, self.contas) #pega o saldo de cada conta da lista de contas(self.contas)

        return max(saldos) #retorna o maior dos saldos

    def menorSaldo(self):
        saldos = map(lambda conta: conta.saldo, self.contas) #pega o saldo de cada conta da lista de contas(self.contas)

        return min(saldos) #retorna o menor dos saldos

    def quantidadeClientes(self):
        return len(self.clientes) #tamanho da lista de clientes


    