# Objetivo: separar as funções de saque, depósito e extrato e 
# criar duas novas funções: usuário e cadastrar conta bancária

import textwrap

def menu ():
    menu = """
    ----------------Menu----------------
    Digite a opção escolhida:
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [lu]\tListar usuários
    [q]\tSair
    -> """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor_depositado, extrato, /):
    # Depósito: 
    # argumentos por positional only (argumentos: saldo, valor, extrato)
    # retorno: saldo e extrato

    if (valor_depositado > 0):
        saldo += valor_depositado
        extrato += f"Depósito: R$ {valor_depositado:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
            
    else: 
        print("\n@@@ Operação falhou! O valor informado não pode ser negativo ou nulo. @@@")

    return saldo, extrato

def sacar(*, saldo, valor_sacado, extrato, limite, numero_saques, limite_saques):
    # Saque:
    # deve receber argumentos keyword only (argumentos: saldo, valor,
    # extrato, limite, numero saques, limite saques)
    # retorno: saldo e extrato

    excedeu_saldo = valor_sacado > saldo
    excedeu_limite = valor_sacado > limite
    excedeu_saques = numero_saques >= limite_saques

    if (excedeu_saldo):
        print("\n@@@ Operação falhou! Você não possui saldo suficiente em conta. @@@")
    elif (excedeu_limite):
        print("\n@@@ Operação falhou! Você só pode sacar até R$ 500.00. @@@")
    elif (excedeu_saques):
        print("\n@@@ Operação falhou! Você já sacou o máximo de saques diários permitidos. @@@")
    elif (valor_sacado > 0):
        numero_saques += 1
        saldo -= valor_sacado
        extrato += f"Saque: R$ {valor_sacado:.2f}\n" 
        print("\n=== Saque realizado com sucesso! ===")
            
    else: 
        print("\n@@@ Operação falhou! O valor informado não pode ser negativo ou nulo. @@@")
    
    return saldo, extrato

def mostrar_extrato(saldo, /, *, extrato):
    # Extrato:
    # argumentos positional only (saldo) e keyword only (extrato)
    print ("----------------Extrato----------------")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print (f"Saldo atual: R$ {saldo:.2f}")
    print("----------------------------------------")

def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def novo_usuario(usuarios):
    # Criar usuário e armazenar em lista: nome, nascimento, cpf (string
    # com somente números) e endereço (logradouro, n°, bairro, cidade/sigla estado)
    # não é possível ter 2 usuáros com o mesmo cpf
    
    cpf = input ("Informe seu CPF (somente números): ")
    usuario = filtrar_usuarios(cpf,usuarios)
    
    if usuario: #se realizou a função de filtrar usuário e retornou um usuário
        print("\n@@@ Já existe um usuário com esse CPF! @@@")
        return
    
    nome = input("Informe seu nome completo: ")
    data_nasc = input("Informe sua data de nascimento: ")
    endereco = input("Endereço (logradouro, n° - bairro - cidade/sigla estado): ")

    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nasc,
        "cpf": cpf,
        "endereco": endereco
    })

    print("=== Usuário criado com sucesso! ===")

def nova_conta(agencia, num_conta, usuarios):
    # Criar conta corrente e armazenar em lista: agência (número fixo 0001), 
    # n° da conta (sequencial, iniciando em 1) e usuário (pode ter mis de uma conta)
    
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario: #se o usuário for encontrado
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": num_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

def listar_contas(contas):
    for conta in contas: #formatacao
        linha = f"""\
            Agência: {conta['agencia']}
            C/C: {conta['numero_conta']}
            Titular: {conta['usuario']['nome']}
        """
        print("=" * 70)
        print(textwrap.dedent(linha))

def listar_usuarios(usuarios):
    for usuario in usuarios:
        linha = f"""\
            Nome: {usuario['nome']}
            Data de nascimento: {usuario['data_nascimento']}
            CPF: {usuario['cpf']}
            Endereço: {usuario['endereco']}
        """
        
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    saldo = 0
    limite_diario = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    usuarios = []
    contas = []

    while True:

        opcao = menu()

        
        if opcao == "d":
            print("--------------------------------Depósito--------------------------------")
            print("Observação: Separe os centavos por um ponto (.)\n")
            valor_depositado = float(input("Digite o valor que irá depositar: R$ "))
            
            saldo, extrato = depositar(saldo, valor_depositado, extrato)


        elif opcao == "s":
            print("--------------------------------Saque--------------------------------")
            print("Observação: É possível realizar até 3 saques diários, com o limite de valor de R$ 500.00 em cada.\n")
            valor_sacado = float(input("Digite o valor que deseja sacar: R$ "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor_sacado=valor_sacado,
                extrato=extrato,
                limite=limite_diario,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
           mostrar_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            novo_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = nova_conta(AGENCIA, numero_conta, usuarios)

            if conta: #se a conta foi criada com sucesso, irá fazer o append
                contas.append(conta)
        
        elif opcao == "lc":
            contas = listar_contas(contas)

        elif opcao == "lu":
            usuarios = listar_usuarios(usuarios)

        elif opcao == "q":
            break

        else: print("Operação inválida, por favor selecione novamente a operação desejada.")


main()