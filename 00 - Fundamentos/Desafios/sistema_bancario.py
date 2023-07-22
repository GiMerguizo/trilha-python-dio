from time import sleep
''' 
Operações: depósito, saque, extrato
Depósito:
    - Depositar valores positivos
    - Somente 1 usuário
    - Armazenar em 1 variável e exibir no extrato
Saque:
    - 3 saques diários
    - Limite: R$ 500,00 por saque
    - Sem saldo: exibir mensagem
    - Armazenar em uma variável e exibir no extrato
Extrato:
    - Listar todos os depósitos e saques
    - Exibir o saldo atual
    - Formato: R$ 1500.45
'''

menu = """
------- MENU -------
    [1] Depósito
    [2] Saque
    [3] Extrato
    [4] Sair
--------------------

Opção: """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    print(f'\nOpção selecionada: {opcao}\n')
    sleep(2)

    if opcao == "1":
        print('Depósito\n')
        deposito = float(input('Valor: '))

        if deposito > 0:
            extrato += f' + R$ {deposito:.2f}\n '
            saldo += deposito
        else:
            print('Valor inválido! Tente novamente.')
    
    elif opcao == "2":
        print('Saque\n')

        if numero_saques >= LIMITE_SAQUES:
            print(f'Número diário máximo de saques excedido ({LIMITE_SAQUES}).')
        else:
            saque = float(input('Valor: '))
            
            if saque > saldo:
                print('Saldo insuficiente! Tente novamente.')
            elif saque > limite:
                print(f'Valor máximo permitido: R$ {limite:.2f}. Tente novamente.')
            elif saque > 0:
                numero_saques += 1
                extrato += f' - R$ {saque:.2f}\n '
                saldo -= saque
            else:
                print('Valor inválido! Tente novamente.')
            
    elif opcao == "3":
        print('Extrato\n')
        print("Não foram realizadas movimentações." if not extrato else f'Extrato:\n{extrato}')
        # print(f'Extrato:\n{extrato}')
        print(f'\nSaldo final: R$ {saldo:.2f}')

    elif opcao == "4":
        print('Encerrando programa...\n')
        sleep(2)
        break

    else:
        print('Operação inválida! Por favor, selecione novamente a opção desejada.')
