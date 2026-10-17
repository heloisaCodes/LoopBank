from conta import listarContas


def montanteBanco(contas):
    montanteSaldo = 0
    contas = listarContas(contas)    #lista de todas as contas
    for conta in contas:
        montanteSaldo += conta["saldo"]    #pega o saldo de cada conta e vai somando

    return montanteSaldo             #o dinheiro total de todas as contas



def montanteAgencia(contas, agencias):     #pega a lista agencias
    contas = listarContas(contas)          #lista de todas as contas
    resultados = []

    for agencia in agencias:     # para cada agencia da lista agencias

        contadorAgencia = 0

        for conta in contas:    #ler as contas
            if conta["agencia"] == agencia:    #se a agencia da conta atual for a mesma da agencia lida no momento
                quantClientes = len(conta["clientes"])    #pega a quatidade de clientes vinculados aquela conta
                contadorAgencia += quantClientes    #soma isso a quantidade de clientes da agencia
            # faz isso para todas as contas

#adiciona um dicionario à lista com agencias e a quantidade de clientes vinculados a ela
        resultados.append({"agencia": agencia, 
                           "quantidadeClientes": contadorAgencia
                           })   

#vê se a lista ta vazia
        if not resultados:
            return resultados, None  #se tiver, nao existe agencia para comparar
   
 #aqui considera a 1° agencia como a maior qnt de clientes
    agenciaMaior = resultados[0]    

    for resultado in resultados:    #percorre os resultados de todas as agencias e compara
        if resultado["quantidadeClientes"] > agenciaMaior["quantidadeClientes"]:
            agenciaMaior = resultado  #se agencia atual tiver mais cliente, ela se torna a agencia com maior quantidade
            
    return resultados, agenciaMaior



#calcula o saldo total da conta
def saldoTotal(contas):
    if len (contas) == 0:      #aqui ele verifica se a lista ta vazia
        return 0               #se sim, retorna 0

    
#caso a lista nao esteja vazia, calculamos o saldo total
    saldos = map(lambda conta: conta ["saldo"], contas)  #pega o saldo de cada conta, independentemente se é conta corrente, salario ou poupanca
    saldo_total = sum(saldos)   #soma todos esses valores
    return saldo_total    # retorna um unico valor


#calcula o maior saldo da conta
def maiorSaldo (contas):
    if not contas:       #primeiro vê se a conta ta cadastrada, se nao, retorna 0
        return 0

    
#caso tenha conta cadastrada
    saldos = map(lambda conta: conta["saldo"], contas)
    maior = max(saldos)      #pega o maior saldo
    return maior

    
#calcula o menor saldo da conta, o mesmo raciocinio
def menorSaldo (contas):
    if not contas:
        return 0
    
    saldos = map(lambda conta: conta["saldo"], contas)
    menor = min(saldos)
    return menor

def gerarDashboard(clientes, contas):     #pega os clientes e as contas
  totalClientes = len(clientes)             
  totalContas = len(contas)               #descobre o total de cliente e contas 

  if totalContas == 0:                    #se o total de contas for 0 automáticamente já define os valores como 0 
    totalSaldo = 0.0
    maiorSaldo = 0.0
    saldoMedio = 0.0

  else:
    saldos = [conta['saldo'] for conta in contas]       #percorre contas nos dicionarios com a chave saldo 

    
    totalSaldo = reduce(lambda acumulador, x: acumulador + x, saldos)  #função de alta ordem usando reduce 

    
    maiorSaldo = reduce(lambda a, b: a if a > b else b, saldos)     #retorna o maior valor entre a e b 

    saldoMedio = totalSaldo / totalContas       #faz a divisão para descobrir o saldo medio 

  print("=" * 40)
  print("      DASHBOARD FINANCEIRO LOOPBANK     ")
  print("=" * 40)
  print(f"Número de clientes cadastrados : {totalClientes}")                    #organização do dashboard
  print(f"Número de contas ativas        : {totalContas}")
  print(f"Saldo total no banco       : R$ {totalSaldo:,.2f}")
  print(f"Maior saldo individual         : R$ {maiorSaldo:,.2f}")
  print(f"Saldo médio por conta          : R$ {saldoMedio:,.2f}")
  print("=" * 40)

  return {                            #retorna o que foi calculado 
      'totalClientes': totalClientes,
      'totalContas': totalContas,
      'totalSaldo': totalSaldo,
      'maiorSaldo': maiorSaldo,
      'saldoMedio': saldoMedio,
  }



    

    



