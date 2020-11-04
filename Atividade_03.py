# Exercício 01: Elabore um programa que imprima na tela uma contagem regressiva de 10 até 0
for a in range(10, -1, -1):
    print(a)
print('FIM\n')

# Exercício 02: Elabore um programa que calcule e exiba a soma de todos os números pares entre 0 e 10
soma = 0
for b in range(0, 11, 2):
    soma = soma + b
print(f'A soma de todos números pares de 0 a 10 é: {soma}\n')

# Exercício 03: Elabore um programa que exiba automaticamente a tabuada de um número informado pelo usuário.
c = int(input('Digite um número para ver sua tabuada: '))
for multiplicador in range(0, 11):
    print(f'{c} x {multiplicador} = {c * multiplicador}')
print(f'Fim da tabuada do número {c}\n')

# Exercício 04: Elabore um programa que leia o ano de nascimento de 5 pessoas
# Calcule a idade (anoATUAL – anoNASCIMENTO)
# Contabilize quantos são idosos (acima 60)
contador = 0
ano_atual = int(input('Digite o ano atual: '))
for d in range(0, 5):
    ano_nasc = int(input(f'Digite o {d+1}o ano de nascimento: '))
    if (ano_atual - ano_nasc > 60):
        contador = contador + 1
print(f'A quantidade de idosos é de {contador}.\n')

# Exercício 05: Elabore um programa que leia o peso de 5 pessoas
# Informe o mais pesado
# Informe o mais leve
pesado = 0
leve = 10000
peso = 0
for i in range(0, 5):
    peso = int(input(f'Digite o {i+1}o peso: '))
    if (peso > pesado):
        pesado = peso
    if (peso < leve):
        leve = peso
print(f'O mais pesado: {pesado}kg\nO mais leve: {leve}kg\n')

# Desafio for: Descobrir se um número digitado é primo
num_primo = int(input('Digite um número: '))
aux = 0
for i in range(1, num_primo + 1):
    if ((num_primo % i) == 0):
        aux = aux + 1
if aux == 2:
    print(f'O número {num_primo} é primo.\n')
else:
    print(f'O número {num_primo} não é primo.\n')

# Exercício 06: Elabore um programa que leia números inteiros até que seja digitado algum inteiro negativo
# Ao final deve apresentar quantos números são: PAR e ÍMPAR

n1 = 0
par = 0
impar = 0
while (n1 >= 0):
    n1 = int(input('Digite um número: '))
    if (n1 > 0):        # Excluindo zero e números negativos da verificação de pares ou ímpares
        if (n1 % 2 == 0):
            par = par + 1
        else:
            impar = impar + 1
print(f'A quantidade de pares foi {par} e de ímpares foi de {impar}.\n')

# Exercício 07: Jogo de adivinhação
# O PC escolhe um número entre 0 e 10. Sem o jogador saber qual é este número e guarde numa variável.
# O jogador deve ir dando palpites até acertar o número escolhido pelo PC.
# No final, apresente quantas tentativas foram necessárias até acertar.

import random
n5 = random.randint(0, 10)
tentativas = 0
palpite = 11
while n5 != palpite:
    palpite = int(input('Digite um númere de 0 a 10: '))
    tentativas = tentativas + 1
print(f'Parabéns! Você acertou o número em {tentativas} chances.\n')

# Exercício 08: Calculadora simples - Faça um programa que leia 2 números inteiros e, em seguida, apresente um menu:
# [1] soma
# [2] subtração
# [3] multiplicação
# [4] divisão
# [0] SAIR
# Faça uma leitura de qual opção foi digitada
# Por fim, realize e exiba a operação escolhida com os 2 números inteiros anteriormente lidos

n2 = int(input('Digite um número: '))
n3 = int(input('Digite outro número: '))
operacao = 1
while (operacao != 0):
    operacao = int(input('[1] Soma\n[2] Subtração\n[3] Multiplicação\n[4] Divisão\n[0] SAIR\nDigite o número da opção: '))
    if (operacao == 1):
        print(f'A soma de {n2} e {n3} é {n2 + n3}.')
    elif (operacao == 2):
        print(f'A subtração de {n2} por {n3} é {n2 - n3}.')
    elif (operacao == 3):
        print(f'A multiplicação de {n2} por {n3} é {n2 * n3}.')
    elif (operacao == 4):
        print(f'A divisão de {n2} por {n3} é {round(n2 / n3, 2)}.')
    elif (operacao == 0):
        print('Saindo da calculadora.')
    else:
        print('Não há opção com o número escolhido, digite uma opção válida de 0 a 4.')
print('FIM\n')

# Desafio while: Descobrir o fatorial de um número.
n4 = int(input('Digite um número: '))
aux = n4
fatorial = 1
while (n4 != 0):
    fatorial = fatorial * n4
    n4 = n4 - 1
print(f'O fatorial de {aux}! é {fatorial}.\n')