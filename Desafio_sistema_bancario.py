import datetime

menu = """

[D] Depositar
[S] Sacar
[E] Extrato
[R] Resumo Extrato
[Q] Sair

=> """

saldo = 0
limite = 500
depositos = ""
saques = ""
numero_saques = 0
LIMITE_SAQUES = 3
total_depositado = 0
total_sacado = 0

while True:

    opcao = input(menu).upper()

    if opcao == "D":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            total_depositado += valor
            data_hora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            depositos += f"{data_hora} - Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação não realizada! O valor informado é inválido.")

    elif opcao == "S":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação não realizada! Saldo insuficiente.")

        elif excedeu_limite:
            print("Operação não realizada! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação não realizada! Limite diário de saque excedido.")

        elif valor > 0:
            saldo -= valor
            total_sacado += valor
            data_hora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            saques += f"{data_hora} - Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "E":
        print("\n================ EXTRATO ==================")
        print("Depósitos:")
        print("Não foram realizados depósitos." if not depositos else depositos)
        print("\nSaques:")
        print("Não foram realizados saques." if not saques else saques)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===========================================")

    elif opcao == "R":
        print("\n=========== RESUMO DO EXTRATO =============")
        print(f"Total Depositado: R$ {total_depositado:.2f}")
        print(f"Total Sacado: R$ {total_sacado:.2f}")
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===========================================")

    elif opcao == "Q":
        break

    else:
        print("Opção inválida, por favor selecione novamente as opções do menu.")
