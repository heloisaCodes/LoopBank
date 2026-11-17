class Conta:

    contasCadastradas = {} #atributo de classe
   
    def __init__(self, cliente, cpf, numeroConta, senha=None, saldo=0.0): #construcao da classe com poo
        self.cliente = cliente
        self.cpf = cpf
        self.numeroConta = numeroConta
        self.__senha = senha
        self.saldo = saldo

    def exibirInfo(self):                             #metodo para exibir as info sem exibir a senha
        print(f"Nome:{self.cliente}")
        print(f"Cpf:{self.cpf}")
        print(f"Numero da Conta:{self.numeroConta}")
        print(f"Saldo: R${self.saldo:.2f}")

    @classmethod
    def criarConta(cls, cliente, cpf, numeroConta, senha=None):       #metodo para criar conta com construtor alternativo
        return cls(cliente, cpf, numeroConta, senha=senha, saldo=0.0)
   
    @classmethod
    def podeExcluir(cls, numeroConta):                 #metodo para excluir a conta precisa do prefixo cls. pois é um dicionario
        if numeroConta in cls.contasCadastradas:        #que pertence a classe
            del cls.contasCadastradas[numeroConta]
            return True
        return False
       
    @classmethod
    def listarContas(cls):                    #lista as contas
        return cls.contasCadastradas
       
    def cadastrarConta(self):
        if self.numeroConta in Conta.contasCadastradas: #aqui retorna False se a conta ja esta cadastrada e adiciona se ainda nao esta
            return False
        else:
            Conta.contasCadastradas[self.numeroConta] = self
            return True

    def sacar(self, valorSaque):                      
        if self.saldo < valorSaque or valorSaque <= 0: #retorna False se o valor do saque for maior que o saldo ou saque = 0
            return False
        else:
            self.saldo -= valorSaque                  #reduz o valor do saque do saldo da conta e retorna True
            return True
           
    def depositar(self, valorDeposito):              
        if valorDeposito < 0.01:                     #valor minimo para deposito é de 1 centavo, caso seja menor retora False
            return False
        else:
             self.saldo += valorDeposito             #adiciona o valor do deposito
             return True
           
    def transferir(self, contaDestino, valor):      
        if self.sacar(valor):                        #utiliza o metodo sacar como forma de reduzir o saldo
            contaDestino.depositar(valor)            #utiliza o metodo de depositar para poder transferir para a conta destino
            return True
        return False
       
    def autenticar(self, senhaDigitada):             #verifica se a senha digitada esta correta
        return self.__senha == senhaDigitada