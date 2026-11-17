class Cliente:
    def __init__(self, cpf, nome): 
         # aqui pergunta ao validarCpf se o cpf é válido
        if not Cliente.validarCpf(cpf):   # como ele é um método da classe, chamamos por Cliente.validarCpf
            raise ValueError("CPF inválido") # nenhum cliente é criado com cpf inválido

        # só chega aqui se o cpf passou na validaçao
        self.cpf = cpf      # guarda o cpf e o nome
        self.nome = nome    

        # de objeto PARA dicionário (usado ao SALVAR)
    # usa self porque converte ESTE cliente específico
    def paraDicionario(self):
        return {
            "nome": self.nome,
            "cpf": self.cpf
        }

        # de diicionário PARA objeto (usado ao CARREGAR)
    # @classmethod porque ainda não existe objeto quando chamamos
    @classmethod
    def deDicionario(cls, dados):  # "cls" é no caso a própria classe 
        return cls(dados["nome"], dados["cpf"]) # ent ele cria um cliente novo a partir dos dados do dicionário


    # precisa do self porque muda os dados DESTE cliente
    def editarNome (self, novoNome):
        self.nome = novoNome


    @staticmethod 
    def validarCpf(cpf): # ja que nao depende de nenhum cliente, não precisa do self
        # aqui ja são os códigos de antes, que ja existia na validação

         #verifica se todos os caracteres são números / ib: duda
            for caractere in cpf:
                    if caractere < "0" or caractere > "9":
                        return False
                    
            # Verifica se o cpf tem 11 caracteres ou se possui todos os dígitos iguais
            if len(cpf) != 11 or cpf == cpf[0] * 11:
                return False
            
            # Acumuladores inicializados
            soma1 = 0
            soma2 = 0
        
            # Verificação do penúltimo dígito
            for i in range(0, 9):
                soma1 += int(cpf[i]) * (10 - i)
        
            resto1 = soma1 % 11
            if resto1 == 0 or resto1 == 1:
                digito1 = 0
            else:
                digito1 = 11 - resto1
        
            # Verificação do último dígito
            for i in range(0, 10):
                soma2 += int(cpf[i]) * (11 - i)
        
            resto2 = soma2 % 11
            if resto2 == 0 or resto2 == 1:
                digito2 = 0
            else:
                digito2 = 11 - resto2
        
            return digito1 == int(cpf[9]) and digito2 == int(cpf[10])