class Agencia:

    def __init__(self, numero, clientes, contas):
        self.numero = numero
        self.clientes = clientes
        self.contas = contas

    
    def adicionarCliente(self, cliente):
       self.clientes.append(cliente) #adicona o objeto cliente criado a lista

    def excluirCliente(self, cpf):
       cliente = self.procurarCliente(cpf)

       if cliente:
           contasCliente = self.procurarContasCliente(cpf) #pega as contas do cliente
           for conta in contasCliente: #para cada conta do cliente
               if not conta.podeExcluir(): #verifica se pode excluir
                   return False #se não puder, o cliente não é excluido

           for conta in contasCliente: #se puder, segue e o cliente é excluido
               self.contas.remove(conta) #sai da lista contas
            
           self.clientes.remove(cliente) #sai da lista clientes
                    
           return True

       else:
           return False

    def editarCliente(self, cpf, novoNome):
       cliente = self.procurarCliente(self, cpf)

       if cliente:
          cliente.editarNome(novoNome) #altera o nome do cliente especifico, pelo método de cliente que altera o nome de um objeto qualquer
          return True

       return False


    def adicionarConta(self, conta):
        self.contas.append(conta)


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
    def procurarPorCpf(self, cpf):
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