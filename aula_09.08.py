# Impressão com máscara versão 2 →
n1 = int(input('Digite o número 1: '))
n2 = int(input('Digite o número 2: '))
s = n1 + n2
print(f'A soma de {n1} com {n2} é igual a {s}')

# Testando operadores
n3 = 5
n4 = 2
print(f'Soma = {n3+n4}')
print(f'Subtração = {n3-n4}')
print(f'Multiplicação = {n3*n4}')
print(f'Divisão = {n3/n4}')
print(f'Soma = {n3+n4}; Subtração = {n3-n4}; Multiplicação = {n3*n4}; Divisão = {n3/n4}')
print(f'Potência = {n3**n4}')
print(f'Divisão inteira = {n3//n4}')
print(f'Resto = {n3%n4}')           # Método para avaliar se é par ou ímpar, pelo resto =0 ou =1.
print(f'Potência = {n3**n4}; Divisão inteira = {n3//n4}; Resto = {n3%n4}')

# Números grandes são limitados pela RAM
print(2 ** 5555)                # Usa o tamanho da RAM disponível
print(f'{10/3:.2f}')            # 2 casas decimais
print(f'{10/3:.10f}')           # 10 casas decimais

# Strings podem usar operadores aritméticos
print('Lucca' + ' Altomani')
print('Lucca'*3)
print('='*20)