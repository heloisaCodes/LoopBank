from datetime import date              #importa a classe date para termos datas
from conta import Conta                #importa a classe conta 


class ContaPoupanca(Conta):            #cria a classe conta poupanca herdando conta
    def __init__(self, cliente, cpf, numeroConta, senha=None, saldo=0.0, taxa=0.005, dataAbertura=None):  #construção da classe 
        super().__init__(cliente, cpf, numeroConta, senha=senha, saldo=saldo)
        self.tipo = 'poupança'                                                       #definicao do tipo da conta
        self.taxa = taxa                                                             
        hoje_iso = date.today().isoformat()                                          
        self.dataAbertura = dataAbertura if dataAbertura else hoje_iso               #utilizacao da data informada ou data de hoje
        self.ultimoRendimento = self.dataAbertura                                    #definicao da data inicial para saber o rendimento da poupanca

    def exibirInfo(self):                                                            #metodo para exibir informacoes
        super().exibirInfo()
        print(f"Tipo: {self.tipo}")
        print(f"Taxa de Rendimento: {self.taxa * 100:.2f}%")
        print(f"Último Rendimento: {self.ultimoRendimento}")

    def rendimento(self):                                         
        aumento = self.saldo * self.taxa                           #calculo do rendimento 
        self.saldo = round(self.saldo + aumento, 2)                #soma com o saldo e arredonda o valor 
        return self.saldo                                          #retorna o saldo atualizado 

    def verificarRendimento(self):                                   #metodo para ver se o tempo ja é suficiente para render 
        hoje = date.today()                                         
        ultimo_rendimento_data = date.fromisoformat(self.ultimoRendimento)            
        dias = (hoje - ultimo_rendimento_data).days                                #calculo da diferenca de dias desde o ultimo rendimento

        if dias >= 30:                                                       #verificacao se chegou em 30 dias ou mais 
            self.rendimento()                                               #adiciona o rendimento no saldo
            self.ultimoRendimento = hoje.isoformat()                        #atualiza a data 
            return True                                                     #retorna True se teve rendimento e False caso contrario 
        return False