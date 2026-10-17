from conta import listarContas



def montanteBanco(contas):
    montanteSaldo = 0
    contas = listarContas(contas)    #lista de todas as contas
    for conta in contas:
        montanteSaldo += conta[3]    #pega o saldo de cada conta e vai somando

    return montanteSaldo             #o dinheiro total de todas as contas



def montanteAgencia(contas, agencias):     #pega a lista agencias
    contas = listarContas(contas)          #lista de todas as contas
    resultados = []

    for agencia in agencias:     # para cada agencia da lista agencias

        contadorAgencia = 0

        for conta in contas:    #ler as contas
            if conta[0] == agencia:    #se a agencia da conta atual for a mesma da agencia lida no momento
                quantClientes = len(conta[4])    #pega a quatidade de clientes vinculados aquela conta
                contadorAgencia += quantClientes    #soma isso a quantidade de clientes da agencia
            # faz isso para todas as contas

        resultados.append((agencia, contadorAgencia))    #depois salva a quantidade aquela agencia, e vai para a proxima


    #descobrir a agencia com a maior quantidade de clientes

    maiorQuantClientes = resultados[0][1]    #define uma quantidade de clientes por agencia como maior
    agenciaMaior = resultados[0]    # e sua respectiva agencia como a maior

    for resultado in resultados:    #percorre cada tupla

        quantClientes = resultado[1]    #analisa somente o contadorAgencia
        if maiorQuantClientes >= quantClientes: 
            agenciaMaior = agenciaMaior
        else:
            agenciaMaior = resultado
            maiorQuantClientes = quantClientes
            
    return resultados, agenciaMaior

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

        

    



