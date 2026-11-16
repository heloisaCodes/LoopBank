class Agencia:

    def __init__(self, numero, clientes, contas):
        self.numero = numero
        self.clientes = clientes
        self.contas = contas


#RELATORIO

    #soma todos os saldos
    def montante(self): #como temos apenas 1 agência, correponde ao saldo de todas as contas da agencia/banco
        montante = 0
        for conta in self.contas: #soma o saldo de cada conta
            montante += conta.saldo

        return montante

    def maiorSaldo(self):
        saldos = list(map(lambda conta: conta.saldo, self.contas)) #pega o saldo de cada conta da lista de contas(self.contas)

        return max(saldos) #retorna o maior dos saldos

    def menorSaldo(self):
        saldos = list(map(lambda conta: conta.saldo, self.contas)) #pega o saldo de cada conta da lista de contas(self.contas)

        return min(saldos) #retorna o menor dos saldos

    def quantidadeClientes(self):
        return len(self.clientes) #quantidade de clientes na lista de clientes

#LISTA E BUSCA

    def listarClientes(self):
        return self.clientes 


    def listarContas(self):
        return self.contas
    

    def listar_ContasPositivas(self):
        contasPositivas = list(filter(lambda conta: conta.saldo > 0, self.contas)) #filtra as contas com saldo positivo e armazena numa lista

        return contasPositivas

    def procurarCliente(self, cpf):
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                return cliente

        return False

    #procura as contas do cliente
    def procurarPorConta(self, cpf):
        contasCliente = [] 
        for conta in self.contas:                  
            if cpf == conta.titular: 
                contasCliente.append(conta)

        return contasCliente


    def procurarPorConta(contas, numerodacontadigitado):
        for conta in contas:                                    
            if numerodacontadigitado == conta.numerodaconta:
                return conta 
            
        return False