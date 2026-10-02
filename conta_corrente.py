import conta

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
    novo_saldo = conta.deposito(     
        conta["saldo"],
        valor
    )

    conta["saldo"] = novo_saldo 
    return True

 # mesma ideia do saque, aqui ver quanto a pessoa tem disponivel levando em consideracao o limite
def saque(conta, valor):           
    disponivel = limite_disponivel(conta)

    if valor > disponivel:
        return False

    conta["saldo"] -= valor      # se tiver valor suficiente, diminuimos o valor do saque do saldo
    return True


def transferir(conta, conta_destino, valor):   # o que ja tem em conta, foi usado a msm logica
    resultado = conta.transferir(              # chama a funcao transferir que ta em conta
        conta,
        conta_destino,
        valor
    )

    return resultado


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

