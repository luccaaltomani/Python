# Exercício 01: Faça um programa para calcular a média ponderada de 2 notas, sendo 40% para a primeira e 60% para a segunda.
n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
mp = (n1*0.4 + n2*0.6)/(0.4+0.6)
print(f'A média ponderada das notas {n1} e {n2} é de {mp}.')

# Exercício 02: Faça um algoritmo para calcular e exibir o consumo de combustível, sendo: consumo = km/litros
km = float(input('Digite quantos quilômetros foram percorridos: '))
l = float(input('Digite quantos litros foram consumidos: '))
c = km/l
print(f'A média do consumo de combustível, tendo percorrido {km}km e consumido {l}L, é de {c}km/L.')

# Exercício 03: Faça um programa para calcular e exibir o IMC, sendo: IMC = peso/altura²
peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em metros: '))
IMC = peso/(altura**2)
print(f'O seu IMC é calculado através da razão de {peso}kg e o quadrado da altura {altura}m e resulta em {IMC}kg/m².')
print('Confira abaixo a lista de situações de acordo com o seu IMC:')
print('Abaixo de 17: Muito abaixo do peso;')
print('Entre 17 e 18.49: Abaixo do peso;')
print('Entre 18.5 e 24.99: Peso normal;')
print('Entre 25 e 29.99: Acima do peso;')
print('Entre 30 e 34.99: Obesidade I;')
print('Entre 35 e 39.99: Obesidade II (severa);')
print('Acima de 40: Obesidade III (mórbida)')

# Exercício 04: Faça um programa que, dada uma quantidade X de dias, calcule a quantidade equivalente em horas.
dias = int(input('Digite o número de dias: '))
horas = dias*24
print(f'A quantidade em horas de {dias} dias é de {horas} horas.')

# Exercício 05: Faça um programa que receba o salário de um funcionário. Calule e mostre o novo salário, sabendo-se que este sofreu um aumento de 25%.
salario = float(input('Digite o seu salário atual: '))
novo_salario = salario*1.25
print(f'Seu novo salário será de {round(novo_salario, 2)} reais.')              # round() ajusta os decimais de um número/variável

# Exercício 06: Faça um programa que dado um valor, apresente: seu antecessor, sucessor, quadrado e raiz.
n3 = int(input('Digite um número inteiro: '))
print(f'O número escolhido foi {n3}, seu antecessor é {n3-1}, o sucessor é {n3+1}, o quadrado {n3**2} e a raiz {n3**(1/2)}.')

# Exercício 07: Faça um programa que leia uma quantidade X em metros e retorne o equivalente em cm e mm.
metros = float(input('Digite o valor em metros: '))
print(f'O valor de {metros}m em cm é de {metros*100}cm e em mm é de {metros*1000}mm.')

# Exercício 08: Faça um programa que dado um valor em reais, mostre quantos dólares a pessoa poderia comprar.
reais = float(input('Digite a quantidade em reais: '))
print(f'A quantidade em dólares que você pode comprar com R${reais} é de ${round(reais/5.2978, 2)}.')

# Exercício 09: Faça um programa que leia a largura e altura de uma parede, em seguida calcule a área (m²), quantidade em litros de tinta necessária para pintar, sabendo que 100ml pinta 2m².
largura = float(input('Digite a largura da parede em metros: '))
altura_p = float(input('Digite a altura da parede em metros: '))
print(f'A área da parede é de {round(largura * altura_p, 2)}m² e gasta-se {round((largura * altura_p * 0.1)/2, 3)}L para pintar.')

# Exercício 10: Para cada figura geométrica abaixo, faça um programa que calcule o perímetro e a área de um quadrado, retângulo, círculo e triângulo equilátero.
ladoq = float(input('Informe o tamanho do lado do quadrado: '))
print(f'O perímetro do quadrado é de {4*ladoq} e a área é de {ladoq**2}.')
lador = float(input('\nInforme o tamanho do lado do retângulo: '))
altr = float(input('Informe o tamanho da altura do retângulo: '))
print(f'O perímetro do retângulo é de {2*(lador+altr)} e a área é de {lador*altr}.')
raioc = float(input('\nInforme o tamanho do raio do círculo: '))
print(f'O perímetro do círculo é de {2*3.14*raioc} e área é de {3.14*(raioc**2)}.')
trilado = float(input('\nInforme o tamanho da base do triângulo equilátero: '))
print(f'O perímetro do triângulo equilátero é de {3*trilado} e a área de {round(((trilado**2)*(3**(1/2)))/2, 2)}.')