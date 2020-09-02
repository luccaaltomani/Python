# n1 = input('Digite o número 1: ')
# n2 = input('Digite o número 2: ')
# s1 = n1 + n2
# print('A soma é ', s1)
#
# n3 = input('Digite o número 3: ')
# print(type(n3))                 # Type retorna o tipo de variável
# n4 = input('Digite o número 4: ')
# print(type(n4))
# # A função input recebe somente textos, ou seja, em strings. Por isso no primeiro exemplo resulta em n1n2, união entre n1 e n2.
#
# n5 = int(input('Digite o número 5: '))
# n6 = int(input('Digite o número 6: '))
# s2 = n5 + n6
# print('A soma é ', s2)
# # Ao declarar a varíavel do input como inteiro, a soma funciona normalmente.

# Exemplo: Mostrar idade de alguém daqui 1 ano
nome = (input('Escreva seu nome: '))
idade = int(input('Informe a sua idade: '))
altura = (input('Informe sua altura: '))
print(nome, ', sua idade daqui um ano será de', idade + 1, 'anos.')
print('O meu nome é {}, tenho {} anos, meço {}m e ano que vem terei {} anos.'.format(nome, idade, altura, idade + 1))