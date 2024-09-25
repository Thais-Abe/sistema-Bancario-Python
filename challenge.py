menu = """

[d] Depositar
[s] Sacar 
[e] Extrato
[x] Sair 

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True: 
    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
    elif opcao =='s':
        print("Saque")
    elif opcao =="e":
        print("Extrato")
    elif opcao =="x":
        break
    else:
        print("Operação inválida, por favor seleciona novamente a operação desejada.")