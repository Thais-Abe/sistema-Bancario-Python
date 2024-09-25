menu = """

[d] Depositar
[s] Sacar
[e] extract
[q] Sair

=> """

balance = 0
limite = 500
extract = ""
number_sakes = 0
LIMITE_SAKES = 3


while True:

    option = input(menu)

    if option == "d":
        value = float(input("Informe o value do depósito: "))

        if value > 0:
            balance += value
            extract += f"Depósito: R$ {value:.2f} ------------------ \n"

        else:
            print("Informe um value válido.")

    elif option == "s":
        value = float(input("Informe o value do sake: "))

        if value > balance:
            print("balance insuficiente.")

        elif value > limite:
            print(" O value do sake excede o limite.")

        elif number_sakes >= LIMITE_SAKES:
            print("Número máximo de sakes excedido.")

        elif value > 0:
            balance -= value
            extract += f"sake: R$ {value:.2f}\n"
            number_sakes += 1

        else:
            print("O value informado é inválido.")

    elif option == "e":
        print("\n================ extract ================")
        print("\n")
        print("Não foram realizadas movimentações." if not extract else extract)
        print(f"\nbalance: R$ {balance:.2f}")
        print("==========================================")

    elif option == "q":
        break

    else:
        print("Por favor selecione novamente a operação desejada.")