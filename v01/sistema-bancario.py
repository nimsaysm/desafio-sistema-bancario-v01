# Objetivo: criar um sistema bancário com as operações:

# Digitar D para Depósito, S para Saque e E para Extrato

menu = """

Digite a opção escolhida:
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

-> """

saldo = 0
limite_diario = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    # Depósito: 
    # de valores positivos (erro ao inserir valor negativo)
    # armazenado em uma variável e exibido na operação de extrato

    if opcao == "d":
        print("--------------------------------Depósito--------------------------------")
        print("Observação: Separe os centavos por um ponto (.)\n")
        valor_depositado = float(input("Digite o valor que irá depositar: R$ "))
        
        if (valor_depositado > 0):
            saldo += valor_depositado
            extrato += f"Depósito: R$ {valor_depositado:.2f}\n"
        
        else: 
            print("Operação falhou! O valor informado não pode ser negativo ou nulo.")

    # Saque:
    # o sistema permite 3 saques diários com limite máximo de R$500/saque
    # caso o usuário não tenha saldo em conta, exibir uma mensagem de que
    # não é possível sacar por falta de saldo. Todos os saques devem ser 
    # armazenados em uma variável e exibidos no extrato

    elif opcao == "s":
        print("--------------------------------Saque--------------------------------")
        print("Observação: É possível realizar até 3 saques diários, com o limite de valor de R$ 500.00 em cada.\n")
        valor_sacado = float(input("Digite o valor que deseja sacar: R$ "))

        excedeu_saldo = valor_sacado > saldo
        excedeu_limite = valor_sacado > limite_diario
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if (excedeu_saldo):
            print("Operação falhou! Você não possui saldo suficiente em conta.")
        elif (excedeu_limite):
            print("Operação falhou! Você só pode sacar até R$ 500.00.")
        elif (excedeu_saques):
            print("Operação falhou! Você já sacou o máximo de saques diários permitidos.")
        elif (valor_sacado > 0):
            numero_saques += 1
            saldo -= valor_sacado
            extrato += f"Saque: R$ {valor_sacado:.2f}\n" 
        
        else: 
            print("Operação falhou! O valor informado não pode ser negativo ou nulo.")
    
    # Extrato:
    # lista todos os depósitos e saques e, no final, mostra o saldo atual
    # da conta. Os valores devem seguir o formato R$ xxx.xx

    elif opcao == "e":
        print ("----------------Extrato----------------")
        print (extrato)
        print (f"Saldo atual: R$ {saldo}")
        print("----------------------------------------")
    
    elif opcao == "q":
        break

    else: print("Operação inválida, por favor selecione novamente a operação desejada.")