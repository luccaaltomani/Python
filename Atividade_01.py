# Exercício 01: Faça um programa para calcular a média ponderada de 2 notas, sendo 40% para a primeira e 60% para a segunda.
n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
mp = (n1*0.4 + n2*0.6)/(0.4+0.6)
print(f'A média ponderada das notas {n1} e {n2} é de {mp}.')

Execução 01:
Digite a nota 1: 9.6
Digite a nota 2: 7.25
A média ponderada das notas 9.6 e 7.25 é de 8.19.

# Exercício 03: Faça um programa para calcular e exibir o IMC, sendo: IMC = peso/altura²
peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em metros: '))
IMC = peso/(altura**2)
print(f'O seu IMC é calculado através da razão de {peso}kg e o quadrado da altura {altura}m e resulta em {round(IMC,2)}kg/m².')
print('Confira abaixo a lista de situações de acordo com o seu IMC:')
print('Abaixo de 17: Muito abaixo do peso;')
print('Entre 17 e 18.49: Abaixo do peso;')
print('Entre 18.5 e 24.99: Peso normal;')
print('Entre 25 e 29.99: Acima do peso;')
print('Entre 30 e 34.99: Obesidade I;')
print('Entre 35 e 39.99: Obesidade II (severa);')
print('Acima de 40: Obesidade III (mórbida)')

Execução 03:
Digite seu peso em kg: 78.3
Digite sua altura em metros: 1.77
O seu IMC é calculado através da razão de 78.3kg e o quadrado da altura 1.77m e resulta em 24.99kg/m².
Confira abaixo a lista de situações de acordo com o seu IMC:
Abaixo de 17: Muito abaixo do peso;
Entre 17 e 18.49: Abaixo do peso;
Entre 18.5 e 24.99: Peso normal;
Entre 25 e 29.99: Acima do peso;
Entre 30 e 34.99: Obesidade I;
Entre 35 e 39.99: Obesidade II (severa);
Acima de 40: Obesidade III (mórbida)

# Exercício 07: Faça um programa que leia uma quantidade X em metros e retorne o equivalente em cm e mm.
metros = float(input('Digite o valor em metros: '))
print(f'O valor de {metros}m em cm é de {metros*100}cm e em mm é de {metros*1000}mm.')

Execução 07:
Digite o valor em metros: 12.05
O valor de 12.05m em cm é de 1205.0cm e em mm é de 12050.0mm.

# Exercício 09: Faça um programa que leia a largura e altura de uma parede, em seguida calcule a área (m²), quantidade em litros de tinta necessária para pintar, sabendo que 100ml pinta 2m².
largura = float(input('Digite a largura da parede em metros: '))
altura_p = float(input('Digite a altura da parede em metros: '))
print(f'A área da parede é de {round(largura * altura_p, 2)}m² e gasta-se {round((largura * altura_p * 0.1)/2, 3)}L para pintar.')

Execução 09:
Digite a largura da parede em metros: 3.75
Digite a altura da parede em metros: 2.4
A área da parede é de 9.0m² e gasta-se 0.45L para pintar.

# Exercício 10: Para cada figura geométrica abaixo, faça um programa que calcule o perímetro e a área de um quadrado, retângulo, círculo e triângulo equilátero.
ladoq = float(input('Informe o tamanho do lado do quadrado: '))
print(f'O perímetro do quadrado é de {4*ladoq} e a área é de {ladoq**2}.')
lador = float(input('\nInforme o tamanho do lado do retângulo: '))
altr = float(input('Informe o tamanho da altura do retângulo: '))
print(f'O perímetro do retângulo é de {2*(lador+altr)} e a área é de {lador*altr}.')
raioc = float(input('\nInforme o tamanho do raio do círculo: '))
print(f'O perímetro do círculo é de {round(2*3.14*raioc,3)} e área é de {round(3.14*(raioc**2),3)}.')
trilado = float(input('\nInforme o tamanho da base do triângulo equilátero: '))
print(f'O perímetro do triângulo equilátero é de {3*trilado} e a área de {round(((trilado**2)*(3**(1/2)))/2, 2)}.')

Execução 10:
Informe o tamanho do lado do quadrado: 2
O perímetro do quadrado é de 8.0 e a área é de 4.0.

Informe o tamanho do lado do retângulo: 2.5
Informe o tamanho da altura do retângulo: 4
O perímetro do retângulo é de 13.0 e a área é de 10.0.

Informe o tamanho do raio do círculo: 1.75
O perímetro do círculo é de 10.99 e área é de 9.616.

Informe o tamanho da base do triângulo equilátero: 3
O perímetro do triângulo equilátero é de 9.0 e a área de 7.79.
