from random import randint

saldo = randint(5.00,1250.00)
for n in range(2,-1,-1):
    name = input('Digite seu nome: ')
    password = int(input('Digite sua senha '))
    print('-'*50)
    if name == 'teste' and password == 123:
        print('Acesso liberado')
        action = int(input('''
    Digite o numero de ID do que queira fazer

    ID 1 - Ver Saldo
    ID 2 - Fazer depósito
    ID 3 - Fazer saque
    ID 4 - Sair do sistema
    >>>: '''))
        if action == 4:
            print('-'*50)
            print('Fechando Sistema')
            break
        elif action == 3:
            print('-'*50)
            print(f'Saldo em conta R${saldo:.2f}')
            saque = float(input('Digite o valor do saque: '))
            if saque <= saldo:
                saldo= saldo - saque
                print(f'Saque realizado \nSaldo atual {saldo:.2f}')
                break
            elif saque > saldo:
                print('-'*50)
                print(f'Saldo insuficiente para o saque \nSeu saldo é de R${saldo:.2f}')
                break
        elif action == 2:
            print('-'*50)
            deposito = float(input('Digite o valor do depósito: '))
            print(f'Saldo em conta R${saldo + deposito:.2f}') 
            break
        elif action == 1:
            print(f'{saldo:.2f}')
            break
    elif name != 'teste' or password != 123:
        print(f'Acesso negado \nVocê tem {n} chances para acessar sua conta')
    elif n == 0:
        print('Acesso Bloqueado')
        break
n = input('Clique enter sair')








# - Ver extrato
# - Fazer um deposito
# - Fazer um saque 
# - Sair do sistema 
# - 3  chances para acessar a conta, caso contrario, haverá um 
# bloqueio na conta.(for) 