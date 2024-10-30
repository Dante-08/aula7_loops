# lista = []

# for n in range(1,4):
#     nome = input('Digite seu nome: ')
#     idade = input('Digite sua idade: ')
#     email = input('Digite seu email: ')
#     print(f'{n} cliente adicionado')
#     print('Proximo cadastro')
#     lista += (nome, idade, email)
# print(lista)

# num = int(input('Digite a tabuada desejada: '))
# print(f'Tabuada do {num}')
# for n in range(11):
#     print(f'{num} x {n} = {num*n}')

print('Você tem 3 chances para acertar o numero aleatório')

from random import randint

for n in range(2,-1,-1):
    chute = int(input('Digite um numero: '))
    aleatorio = randint(1,5)
    if chute == aleatorio:
        print('Você acertou em cheio')
        print(f'Faltando {n} chances')
        break
    else:
        print(f'Você tem {n} chances, o numero aleatório era {aleatorio}')
        