print('|=====================================|')
print('|== Bem-vindo à lixeira reciclável! ==|')
print('|=====================================|\n')
print('[1] - Papel')
print('[2] - Plástico')
print('[3] - Vidro')
print('[4] - Metal')
n = int(input('Digite o número correspondente ao material a ser reciclado: '))

while ((n < 1) or (n > 4)):
    print('\nNão há um material correspondente ao número, favor digitar um número válido.')
    print('[1] - Papel')
    print('[2] - Plástico')
    print('[3] - Vidro')
    print('[4] - Metal')
    n = int(input('Digite o número correspondente ao material a ser reciclado: '))

if (n == 1):
    print('Você selecionou [PAPEL], descarte na lixeira de cor azul.')
elif (n == 2):
    print('Você selecionou [PLÁSTICO], descarte na lixeira de cor vermelha.')
elif (n == 3):
    print('Você selecionou [VIDRO], descarte na lixeira de cor verde.')
elif (n == 4):
    print('Você selecionou [METAL], descarte na lixeira de cor amarela.')