menu = """

[1]DEPÓSITO
[2]SAQUE
[3]EXTRATO
[4]SAIR

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITES_SAQUES = 3

while True:
    
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depódito: R$ {valor:.2f}\n"

        else:
            print("O valor informado é invalido.")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))
        
        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite
        
        excedeu_saques = numero_saques >= LIMITES_SAQUES

        if excedeu_saldo:
            print("Não foi posível realizar a transação, saldo insuficiente!")

        elif excedeu_limite:
            print("Não foi possível realizar a transação, o valor do saque excede o limite.")    

        elif excedeu_saques:
            print("Não foi possível realizar a transação, número de saques excedido.")    

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"    
            numero_saques += 1


        else:
            print("O valor informado é invalido.")    

    elif opcao == "3":
        print("\n===============EXTRATO===============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=====================================")

    elif opcao == "4":
        break


    else:

        print("Operação invalida, por favor selecione novamente a operação desejada.")
