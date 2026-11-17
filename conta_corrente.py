from conta import Conta  # importa a classe Conta


class ContaExterna:  # classe simples so pra representar a conta de outro banco
    def __init__(self, banco, agencia, numero_conta):
        self.banco = banco
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.saldo = 0.0

class ContaCorrente(Conta):
    def __init__(self, cliente, cpf, numeroConta, senha=None, saldo=0.0, limite=500.0):
        super().__init__(cliente, cpf, numeroConta, senha=senha, saldo=saldo)  # puxa os atributos da classe Conta
        self.tipo = "corrente"
        self.limite = limite  #limite de cheque especial, por padrao vem 500

    def exibirInfo(self):
        super().exibirInfo()
        print(f"Tipo: {self.tipo}")
        print(f"Limite: R${self.limite:.2f}")
        print(f"Total Disponível: R${self.limite_disponivel():.2f}")

    def saldo_atual(self):
        return self.saldo

    def limite_disponivel(self):
        return round(self.saldo + self.limite, 2)  #junta o saldo que tem com o limite pra saber o total q da pra gastar

    def credito(self, valor):
        if valor <= 0 or valor > self.limite_disponivel():  #ve se tem limite disponivel pra usar
            return False
        self.saldo = round(self.saldo - valor, 2)
        return True

    def sacar(self, valorSaque):
        if valorSaque <= 0 or valorSaque > self.limite_disponivel():  #sobrescreve o sacar da classe conta pq precisa considerar o limite junto
            return False
        self.saldo = round(self.saldo - valorSaque, 2)
        return True

    def transferir(self, contaDestino, valor):
        if self.sacar(valor):                   #usa o sacar dessa classe que olha o limite
            contaDestino.depositar(valor)
            return True
        return False

    def criar_conta_destino(self, banco, agencia, numero_conta):
        return ContaExterna(banco, agencia, numero_conta)  #cria o objeto da conta externa

    def transferir_outro_banco(self, banco_destino, agencia_destino, numero_conta_destino, valor):
        conta_destino = self.criar_conta_destino(
            banco_destino,
            agencia_destino,
            numero_conta_destino
        )
        if not self.sacar(valor):  
            return False
        conta_destino.saldo = round(conta_destino.saldo + valor, 2)  #soma o valor direto no saldo do objeto
        return conta_destino  # retorna o objeto da conta externa ja atualizado