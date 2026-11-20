from cliente import Cliente

class Agencia:

    def __init__(self, clientes):
        self.numero = '0001'
        self.nome = 'Agência Centro'
        self.endereco = 'Avenida Brasil, 112'
        self.clientes = clientes
    
    def adicionarCliente(self, cliente : Cliente): #(cliente : Cliente) -> objeto (cliente) da classe (Cliente) 
       self.clientes.append(cliente) #adiciona a lista clientes

    def getClientes(self): #método para poder consultar/visualizar a lista de clientes
        return self.clientes #apenas devolve a lista