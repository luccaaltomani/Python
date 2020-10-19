# Contar até 5 com for
for a in range(1, 6):
    print(a)
print('FIM\n')

# Contar até 5 com while
b = 1
while (b < 6):
    print(b)
    b = b + 1       # Incrementar o contador na estrutura de repetição
print('FIM\n')

# Verificar par ou ímpar com while
c = 1
while (c <= 10):
    if (c % 2 == 0):
        print(f'{c} é par.')
    else:
        print(f'{c} é ímpar.')
    c = c + 1
print('FIM\n')

# Utilizando break para parar o while
d = 1
while (True):       # while infinito, pois a repetição é infinita devido ao Verdade
    print(f'O valor da variável é {d}')
    if (d == 10):
        break       # se d=10, então a repetição é quebrada
    d = d + 1
print('FIM\n')

# while com input
e = 1
tentativas = 0
while (e != 0):
    e = int(input('Digite um número: '))        # Enquanto o número digitado for diferente de zero o programa continuará
    tentativas = tentativas + 1
print(f'Você digitou {tentativas} números.')
print('FIM\n')

# while com resposta em string
num1 = 0
quantidade = 0
peso = 0
r = 's'
while (r == 's'):        # não funcinou sem comentar tudo acima
    num1 = int(input('Digite o seu peso: '))
    r = str(input('Deseja continuar (s/n): '))      # Enquanto o usuário digitar "s", o programa seguirá o loop
    quantidade = quantidade + 1
    peso = peso + num1
print(f'A quantidade de pesos digitados foi {quantidade}')
print(f'O total dos pesos foi de {peso} e a média foi de {round(peso/quantidade, 2)}.')
print('FIM\n')

# soma de números até digitar -1
num2 = sum1 = 0
while (num2 != -1):
    num2 = int(input(f'Digite um número: '))
    sum1 = sum1 + num2
print(f'A soma dos números foi {sum1+1}.')      # +1 para excluir o -1 de quebra de loop
print('FIM\n')
