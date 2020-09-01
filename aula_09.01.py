nome = 'Chaves'
mensagem = 'ninguém tem paciência comigo'

# Concatenar textos e variáveis: separando por vírgula
print(nome, 'diz', mensagem)            # não precisa usar espaços

# Concatenar textos e variáveis: separando por +
print(nome + 'diz:' + mensagem)
print(nome + ' diz: ' + mensagem)           # precisa usar espaços

#######################

# A entrada de dados é realizada pela função input(), porém é necessário solicitar qual dado será digitado. O input()
# já permite escrever um texto, cuja resposta será atribuída à variável
nome = input('Olá, qual o seu nome? ')
print('Seja bem-vindo,', nome)
