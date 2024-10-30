

password = input('Digite sua senha: ')

for n in range(2,-1,-1):
    password = input('Digite sua senha: ')
    if password == '123':
        saldo = 1000.00
        print('Acesso Liberado')
        i = int(input('''
        Digite 1 - Ver Saldo
        Digite 2 - Ver extrato
        Digite 3 - Sacar dinheiro
        Digite 4 - Sair do sistema
        >>> '''))
        if i == 1:
            print(saldo)
        elif i == 2:
            print(extrato)
        elif i == 3:
            saque = int(input('Valor do saque: '))
            saldo = saldo - saque
            print(f'Saldo atual {saldo}')
            extrato.append()
            if saque > saldo:
                print('Seu saldo é insuficiente para esse saque')
    elif password != '123':
        print(f'Você tem {n} chances para acessar sua conta')
        if n == 0:
            print('Acesso Bloqueado')
            
        


    
    

