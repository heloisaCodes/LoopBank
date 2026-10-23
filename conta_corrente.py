import conta as modulo_conta  # importa o arquivo conta.py com o apelido "modulo_conta", pra nao confundir com a variavel "conta" (o dicionario da conta do cliente)

def criarContaCorrente(conta, limite = 500):  # vai pegar o que ja existe em conta e apenas adicionar mais caracteristica pra ser uma conta corrente
    conta["tipo"] = "corrente"
    conta["limite"] = limite   # que é o limite que ela pode usar
    return conta


def saldo_atual (conta):
   return conta["saldo"]   # porque o saldo ja ta guardado dentro do dicionario

def limite_disponivel(conta):   
    saldo = conta["saldo"]       # primeiro pegamos o saldo que a pessoa tem
    limite = conta["limite"]     # depois o limite dela
    disponivel = saldo + limite  # o valor disponivel seria a soma deles
    return disponivel
# entao se o cliente tiver 100 em saldo e 500 no limite, ele pode movimenar 600 reais ate esse momento


def credito(conta, valor):         # pra usar limite
    disponivel = limite_disponivel(conta)  # vê quanto a pessoa ainda pode usar

    if valor > disponivel:     # nao permite fazezr se o valor for maior que a do disponivel
        return False

    conta["saldo"] -= valor    # se tiver como, diminuimos o valor do saldo 
    return True


# aqui chama a funcao deposito feito antes em conta, pra nao precisar fzr de novo
def deposito(conta, valor):
    if valor <= 0:                  # não aceita valor zero ou negativo
        return False
    conta["saldo"] = modulo_conta.deposito(conta["saldo"], valor)
    return True


 # mesma ideia do saque, aqui ver quanto a pessoa tem disponivel levando em consideracao o limite
def saque(conta, valor):           
    disponivel = limite_disponivel(conta)

    if valor > disponivel:
        return False

    conta["saldo"] -= valor      # se tiver valor suficiente, diminuimos o valor do saque do saldo
    return True


#a funçao antiga só olhava o saldo e ignorava o limite da conta corrente, essa atual ajusta isso
def transferir(conta, conta_destino, valor):
    if valor <= 0:        
        return False
 
    if valor > limite_disponivel(conta):     # saldo + limite, igual ao saque
        return False
 
    conta["saldo"] = round(conta["saldo"] - valor, 2)      # o round arredonda pra 2 casas decimais, para nao aparecer um saldo com varias casas decimais
    conta_destino["saldo"] = round(conta_destino["saldo"] + valor, 2)     # tira o valor do saldo da conta de origem e soma na conta de destino
    return True


# aqui é uma simulacao de outro banco
def criar_conta_destino(banco, agencia, numero_conta):
    conta_destino = {            # cria um dicioario bem simples
        "banco": banco,
        "agencia": agencia,
        "numero_conta": numero_conta,
        "saldo": 0
    }

    return conta_destino
# nao é uma conta ja cadastrada, é mais uma representacao de banco externo pra fazer uma simulacao


def transferir_outro_banco(conta, banco_destino, agencia_destino, numero_conta_destino, valor):
    # representacao da conta que ta no outro banco
    conta_destino = criar_conta_destino(
        banco_destino,
        agencia_destino,
        numero_conta_destino
    )
    # antes de transferir, ver quanto que a conta pode movimentar
    disponivel = limite_disponivel(conta)  
    if valor > disponivel:
        return False

    conta["saldo"] -= valor                # se tiver dinheiro disponivel, retiramos o valor da conta de origem
    conta_destino["saldo"] += valor        # depois coloca esse msm valor na conta de quem recebe
    return conta_destino

