# Exercício 06: Elabore um programa que leia 3 valores inteiros e informe qual é o MENOR.
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um valor: '))
n3 = int(input('Digite um valor: '))
if ((n1 < n2) and (n1 < n3)):
    print(f'{n1} é o menor.')
elif ((n2 < n1) and (n2 < n3)):
    print(f'{n2} é o menor.')
else:
    print(f'{n3} é o menor.')

# Exercício 07: Faça um programa que leia o salário de um funcionário, calcule e mostre o novo salário, sabendo-se que este sofreu um aumento de:
# 10% para quem recebe até R$ 3500,00
# 5% para quem recebe mais de R$ 3500,00
salario = float(input('Digite o salário: '))
if (salario > 3500):
    print(f'Seu novo salário será de {round(salario*1.05,2)} reais.')
else:
    print(f'Seu novo salário será de {round(salario*1.1,2)} reais.')

# Exercício 09: Escreva um programa que leia o código de um determinado produto e mostre a sua classificação.
codigo = int(input('Digite o código do produto: '))
if (codigo == 1):
    print('Alimento não-perecível.')
elif (2 <= codigo <= 4):
    print('Alimento perecível.')
elif ((codigo == 5) or (codigo == 6)):
    print('Vestuário.')
elif (codigo == 7):
    print('Higiene pessoal.')
elif (8 <= codigo <= 15):
    print('Limpeza e utensílios domésticos.')
else:
    print('Código inválido.')

# Desafio 1: Fazer um jogo de par e ímpar
# Para todos os itens abaixo, O COMPUTADOR:
# 1) pergunta o nome do usuário
# 2) envia uma mensagem de boas vindas com o nome do usuário
# 3) escolhe um número entre 0 e 10 para ele (não relevar ao usuário)
# 4) solicita para o usuário digitar/escolher: 1 (ÍMPAR) ou 2 (PAR)
# 5) revela o seu próprio número
# 6) calcula a soma e apresenta na tela (seu número + número do usuário)
# 7) descobre se a soma é PAR ou ÍMPAR
# 8) informa quem venceu: PC ou nome do usuário
from random import randint
nome = str(input('Digite o seu nome: '))
print(f'Seja bem-vindo(a) ao jogo de par ou ímpar, {nome}!')
pc = randint(0, 10)
escolha = int(input('Digite 1 para escolher ímpar e 2 para escolher par: '))
user = int(input('Digite um número de sua escolha para o jogo: '))
if (((pc+user) % 2 == 0) and (escolha == 2)):
    print(f'A soma de {pc}+{user}={pc+user} é par! Você ganhou, {nome}!')
elif (((pc+user) % 2 != 0) and (escolha == 1)):
    print(f'A soma de {pc}+{user}={pc+user} é ímpar! Você ganhou, {nome}!')
else:
    print(f'Números escolhidos: {pc} e {user}, resultado {pc+user}. Que pena, você perdeu!')

# Desafio 2: Fazer um jogo de JOKENPÔ:
# 1 = pedra
# 2 = papel
# 3 = tesoura
# Para todos os itens abaixo, O COMPUTADOR:
# 1) pergunta o nome do usuário
# 2) envia uma mensagem de boas vindas com o nome do usuário
# 3) escolhe um número entre 1 e 3 para ele (não relevar ao usuário)
# 4) solicita para o usuário digitar/escolher entre 1 e 3
# 5) revela o seu próprio número
# 6) calcula quem ganhou
# 7) informa quem venceu: PC ou nome do usuário
from random import randint
nome = str(input('Digite o seu nome: '))
print(f'Seja bem-vindo(a) ao jokenpô, {nome}!')
pc = randint(1, 3)
user = int(input('Digite 1 para escolher pedra, 2 para escolher papel e 3 para escolher tesoura: '))
if ((user == 1) and (pc == 3)):
    print(f'Você escolheu pedra e o computador tesoura. Parabéns {nome}, você venceu!')
elif ((user == 2) and (pc == 1)):
    print(f'Você escolheu papel e o computador pedra. Parabéns {nome}, você venceu!')
elif ((user == 3) and (pc == 2)):
    print(f'Você escolheu tesoura e o computador papel. Parabéns {nome}, você venceu!')
elif (user == pc):
    print(f'Empate! Você e o computador escolheram o mesmo elemento.')
else:
    print(f'Que pena, você perdeu!')