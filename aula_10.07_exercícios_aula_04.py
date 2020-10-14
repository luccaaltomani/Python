# Exercício 01: Elabore um programa que leia a idade de uma pessoa e informe se ela já pode ou não votar.
idade = int(input('Digite sua idade: '))
if (idade >= 16):
    print('Você já pode votar!')
else:
    print('Você ainda não pode votar!')

# Exercício 02: Elabore um programa que leia um valor inteiro e informe se ele é PAR ou ÍMPAR.
n1 = int(input('Digite um número: '))
if (n1 % 2 == 0):
    print(f'O número {n1} é par!')
else:
    print(f'O número {n1} é ímpar!')

# Exercício 03: Elabore um programa que leia 2 notas, calcule a média aritmética e informe se o aluno está APROVADO ou REPROVADO. Considere APROVADO a MÉDIA ser maior ou igual a 5.
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
if (((nota1+nota2)/2) >= 5):
    print(f'Sua média foi de {((nota1+nota2)/2)} e você foi aprovado(a)!')
else:
    print(f'Sua média foi de {((nota1+nota2)/2)} e você foi reprovado(a)!')

# Exercício 04: Elabore um programa que leia o ano de nascimento de uma pessoa, leia o ano atual, e por fim, informe se ela já pode ou não tirar carteira de motorista. Lembrando que no Brasil a idade mínima para tirar CNH é 18 anos.
nome = str(input('Digite seu nome: '))
ano_nasc = int(input('Digite o ano do seu nascimento: '))
ano_atual = int(input('Digite o ano atual: '))
if ((ano_atual - ano_nasc) >= 18):
    print(f'{nome}, você já pode tirar carteira de motorista.')
else:
    print(f'{nome}, você ainda não tem idade suficiente para tirar carteira de motorista.')

# Exercício 05: Elabore um programa que leia a velocidade de um carro e a velocidade permitida pelo radar. Caso a leitura do carro ser maior que 10% da permitida, informar uma mensagem “reduza a velocidade da próxima vez, porque desta vez terá que pagar uma multa.
v = float(input('Digite a velocidade do veículo: '))
radar = float(input('Digite a velocidade limite: '))
if (v >= (1.1 * radar)):
    print('Reduza a velocidade, você será multado.')
else:
    print('Velocidade dentro do permitido.')

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

# Exercício 08: A Organização Mundial de Saúde classifica as pessoas pela sua faixa etária
idade = int(input('Digite sua idade: '))
if (0 <= idade <= 12):
    print('Criança.')
elif (13 <= idade <= 18):
    print('Adolescente.')
elif (19 <= idade <= 59):
    print('Adulto.')
elif (60 <= idade):
    print('Terceira idade.')
else:
    print('Execute o programa novamente e informe uma idade válida.')

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

# Exercício 10: Elabore um programa que verifique a evaporação do álcool (78,37oC) na destilaria.
temp_alcool = float(input("Digite a temperatura do álcool: "))
if (temp_alcool < 75):
    print("A temperatura está baixa para evaporação.")
elif (75 <= temp_alcool <= 88):
    print("A temperatura está ideal para evaporação.")
elif (temp_alcool > 88):
    print("A temperatura está acima do ideal para evaporação.")
else:
    print("Temperatura inválida.")

# Exercício 11: O valor da conta de energia elétrica deve ser calculado considerando o acréscimo dado pela quantidade consumida, conforme descrito na tabela abaixo:
preco = float(input('Digite o valor do kW/h em reais: '))
consumo = float(input('Digite o consumo em kW/h: '))
if (consumo <= 40):
    print(f'O valor a ser pago com acréscimo é de {round(1.1*preco*consumo,2)} reais.')
else:
    print(f'O valor a ser pago com acréscimo é de {round(1.3*preco*consumo,2)} reais.')

# Exercício 12: Leia 3 números inteiros, em seguida, apresente-os de forma ordenada (crescente), ou seja, do menor para o maior
print('===== Não repita os números =====')
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite um número inteiro: '))
n3 = int(input('Digite um número inteiro: '))
if (n1 > n2 > n3):
    print(f'{n1} - {n2} - {n3}')
elif (n1 > n3 > n2):
    print(f'{n1} - {n3} - {n2}')
elif (n2 > n1 > n3):
    print(f'{n2} - {n1} - {n3}')
elif (n2 > n3 > n1):
    print(f'{n2} - {n3} - {n1}')
elif (n3 > n1 > n2):
    print(f'{n3} - {n1} - {n2}')
elif (n3 > n2 > n1):
    print(f'{n3} - {n2} - {n1}')
else:
    print('Digite números diferentes e tente novamente.')

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
    print(f'A soma de {pc}+{user} é par! Você ganhou, {nome}!')
elif (((pc+user) % 2 != 0) and (escolha == 1)):
    print(f'A soma de {pc}+{user} é ímpar! Você ganhou, {nome}!')
else:
    print(f'Números escolhidos: {pc} e {user}. Que pena, você perdeu!')

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