# while e for

# Sintaxe 'for': for variável in range(início, fim, passo):
# Contar até 6 com for
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

# Pares e ímpares de 1 a 10 com for
for f in range(0, 11, 2):       # Contando zero como par
    print(f)
print('FIM\n')

for g in range(1, 11, 2):
    print(g)
print('FIM\n')

# Lista com for
lista_de_alunos = ['Lucca', 'Amanda', 'João', 'Maria', 'Fulano']
for i in lista_de_alunos:
    print(i)
print('FIM\n')

# Contagem descrescente com for
for h in range(10, 0, -1):      # Ver Linha 3
    print(h)
print('FIM\n')

# Exemplo de range com len()
lista_len = ['Pasta', 'Sabonete', 'Xampu']
for i in range(0, len(lista_len)):
    print(f'Índice: {i}')
for i in lista_len:
    print(f'Produtos: {i}')

# Exemplo 01: Fatorial com for
num3 = int(input('Digite um número para calcular o fatorial: '))
fatorial = 1
for j in range(1, num3 + 1):    # n + 1
    fatorial = fatorial * j
print(f'{num3}! = {fatorial}')

# Exemplo 02: Usar variáveis dentro do laço
inicio = int(input('Digite o início: '))
fim = int(input('Digite o fim: '))
passo = int(input('Digite o passo: '))
for contador in range(inicio, fim, passo):
    print(contador)
print('FIM\n')

# Exemplo 03: Somar valores digitados dentro do for
soma = 0
for k in range(0, 4):       # Pedirá 1 número e o adicionará à 'soma' por iteração, até o fim = 4
    num4 = int(input('Digite um número: '))
    soma = soma + num4
print(f'O valor da soma é {soma}.\nFIM\n')