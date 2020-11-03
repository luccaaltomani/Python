import pygame
import time

# Iniciando pygame
pygame.init()

# Atalhos e definições gerais
img = pygame.image.load
screen = pygame.display.set_mode
clock = pygame.time.Clock()
white = (255, 255, 255)     # Cor branca
black = (0, 0, 0)           # Cor preta
red = (190, 0, 0)           # Cor vermelha
green = (0, 190, 0)         # Cor verde
blue = (0, 0, 190)          # Cor azul
grey = (40, 40, 40)         # Cor cinza
b_red = (255, 0, 0)         # Cor vermelho forte
b_green = (0, 255, 0)       # Cor verde forte
b_blue = (0, 0, 255)        # Cor azul forte
b_grey = (225, 225, 225)    # Cor cinza claro

# Definindo a tela do jogo e seu tamanho em largura x altura (800x600)
display_width = 800
display_height = 600
game_display = screen((display_width, display_height))

# Imagens de fundo (background - bg)
bg_1 = img('bg1.jpg')
bg_2 = img('bg2.jpg')
bg_3 = img('bg3.jpg')

# Título e logo
pygame.display.set_caption('Jogo APS')
icone = img('swords.png')
pygame.display.set_icon(icone)

# Carregando imagens
img_heroi = img('knight.png')
img_dragao = img('dragon.png')
img_amigo = img('elf.png')
img_espada = img('excalibur.png')
img_monstro = img('gargoyle.png')
img_ninja = img('ninja.png')
img_pergaminho_1 = img('scroll.png')
img_pergaminho_2 = img('scrolls.png')
img_sabio = img('wizard.png')
img_bigelf = img('bigelf.png')
img_bigknight = img('bigknight.png')
img_giant = img('giant.png')

# Definindo funções de texto, superfície, capítulos e botões
# Para cada capítulo do jogo foi criada uma função de execução e de botões
def text_objects(text, font):
    text_surface = font.render(text, True, black)
    return text_surface, text_surface.get_rect()

def message_display(text):
    large_text = pygame.font.Font('freesansbold.ttf', 45)
    text_surface, text_rectangle = text_objects(text, large_text)
    text_rectangle.center = ((display_width/2), (display_height/2))
    game_display.blit(text_surface, text_rectangle)

def historia(text, tx, ty):
    normal_text = pygame.font.Font('freesansbold.ttf', 20)
    text_surface, text_rectangle = text_objects(text, normal_text)
    text_rectangle = (tx, ty)
    game_display.blit(text_surface, text_rectangle)

# Definindo botões da página inicial
# button(mensagem, x, y, largura, altura, cor de inativação, cor de ativação, ação)
def button_1(msg1, x1, y1, w1, h1, ic1, ac1, action1 = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x1 + w1 > mouse[0] > x1 and y1 + h1 > mouse[1] > y1:
        pygame.draw.rect(game_display, ac1, (x1, y1, w1, h1))
        if click[0] == 1 and action1 != None:
            if action1 == 'play':
                prologo()
            elif action1 == 'quit':
                pygame.quit()
                quit()
    else:
        pygame.draw.rect(game_display, ic1, (x1, y1, w1, h1))

    small_text = pygame.font.Font('freesansbold.ttf', 20)
    text_surface, text_rectangle = text_objects(msg1, small_text)
    text_rectangle.center = (x1 + (w1 / 2), y1 + (h1 / 2))  # x + meio x, y + meio y -> para centralizar
    game_display.blit(text_surface, text_rectangle)

# Definindo a tela inicial do jogo
def game_introducao():
    introducao = True
    while introducao:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        game_display.fill(b_grey)
        large_text = pygame.font.Font('freesansbold.ttf', 60)
        text_surface, text_rectangle = text_objects('Jogo APS', large_text)
        text_rectangle.center = ((display_width / 2), (display_height / 2))
        game_display.blit(text_surface, text_rectangle)

        button_1('JOGAR', 150, 450, 100, 50, green, b_green, 'play')
        button_1('SAIR', 550, 450, 100, 50, red, b_red, 'quit')

        pygame.display.update()
        clock.tick(60)

def prologo():
    game_display.fill(b_grey)
    historia('Nos tempos medievais existia um herói', 40, 100)
    historia('que era aclamado e amado pelo seu povo,', 40, 125)
    historia('porém existia uma pessoa com inveja do Herói.', 40, 150)
    historia('Nada mais nada menos do que o mago mais poderoso de Locketall', 40, 175)
    historia('e também seu melhor e mais confiável amigo.', 40, 200)
    historia('Após o herói voltar de uma aventura, Mestre dos magos o', 40, 225)
    historia('recebe com um banquete para comemorar sua volta,', 40, 250)
    historia('o que o herói não sabia era o destino que o aguardava…', 40, 275)
    historia('Mestre dos magos jogou uma maldição no vinho do Grande Herói…', 40, 300)
    historia('Após tomar seu vinho, logo em seguida o herói estava no chão.', 40, 325)
    historia('Após 100 anos, o herói acorda perto de sua cidade sem memórias,', 40, 350)
    historia('apenas com sua espada dourada.', 40, 375)
    historia('O jogo prosseguirá sozinho em jornadas de texto, aguarde.', 160, 510)
    pygame.display.update()
    time.sleep(35)
    intro_cap_1()

def intro_cap_1():
    game_display.fill(b_grey)
    historia('O Herói acorda sem entender o que está acontecendo,', 40, 100)
    historia('acompanhado de um antigo amigo.', 40, 125)
    historia('O herói encontra uma masmorra e começa a busca', 40, 150)
    historia('pelas suas memórias explorando a masmorra.', 40, 175)
    pygame.display.update()
    time.sleep(8.5)
    capitulo_1()

def button_2(msg2, x2, y2, w2, h2, ic2, ac2, action2 = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x2 + w2 > mouse[0] > x2 and y2 + h2 > mouse[1] > y2:
        pygame.draw.rect(game_display, ac2, (x2, y2, w2, h2))
        if click[0] == 1 and action2 != None:
            if action2 == 'continuar':
                game_display.fill(b_grey)
                historia('O herói entra na masmorra e se encontra', 40, 100)
                historia('com um monstro guardião do primeiro andar.', 40, 125)
                pygame.display.update()
                time.sleep(5)
                capitulo_2()
            elif action2 == 'quit':
                pygame.quit()
                quit()
    else:
        pygame.draw.rect(game_display, ic2, (x2, y2, w2, h2))

    small_text = pygame.font.Font('freesansbold.ttf', 20)
    text_surface, text_rectangle = text_objects(msg2, small_text)
    text_rectangle.center = (x2 + (w2 / 2), y2 + (h2 / 2))  # x + meio x, y + meio y -> para centralizar
    game_display.blit(text_surface, text_rectangle)

def capitulo_1():
    cap_1 = True
    while cap_1:

        game_display.fill(b_grey)
        game_display.blit(bg_1, (0, 0))
        game_display.blit(img_bigknight, (140, 250))
        game_display.blit(img_bigelf, (480, 250))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        small_text = pygame.font.Font('freesansbold.ttf', 20)
        text_surface, text_rectangle = text_objects('', small_text)
        text_rectangle.center = ((display_width / 2), (display_height / 2))
        game_display.blit(text_surface, text_rectangle)

        button_2('ENTRAR NA MASMORRA', 150, 50, 265, 50, b_grey, white, 'continuar')
        button_2('SAIR', 550, 50, 100, 50, red, b_red, 'quit')

        pygame.display.update()
        clock.tick(60)

def button_3(msg3, x3, y3, w3, h3, ic3, ac3, action3 = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x3 + w3 > mouse[0] > x3 and y3 + h3 > mouse[1] > y3:
        pygame.draw.rect(game_display, ac3, (x3, y3, w3, h3))
        if click[0] == 1 and action3 != None:
            if action3 == 'lutar':
                game_display.fill(b_grey)
                historia('O herói luta bravamente contra o guardião do primeiro', 40, 100)
                historia('andar e vence! Agora seguirá ao terceiro andar', 40, 125)
                pygame.display.update()
                time.sleep(5)
                game_display.fill(b_grey)
                historia('Após passar do primeiro andar, o herói', 40, 100)
                historia('encontra-se com uma aventureira.', 40, 125)
                historia('O local está repleto de pergaminhos ancestrais', 40, 150)
                historia('que contam um pouco da história da masmorra.', 40, 175)
                pygame.display.update()
                time.sleep(8.5)
                capitulo_3a()
            elif action3 == 'conversar':
                game_display.fill(b_grey)
                historia('O herói questiona o guardião sobre o que é a masmorra', 40, 100)
                historia('e o guardião diz que ele repentinamente apareceu', 40, 125)
                historia('do seu mundo e foi obrigado a resguardar o primeiro', 40, 150)
                historia('andar da masmorra. Tranquilamente ele pede ao herói', 40, 175)
                historia('para que descubra os mistérios da masmorra e o liberte.', 40, 200)
                pygame.display.update()
                time.sleep(10)
                game_display.fill(b_grey)
                historia('Após passar do primeiro andar, o herói', 40, 100)
                historia('encontra-se com uma aventureira.', 40, 125)
                historia('O local está repleto de pergaminhos ancestrais', 40, 150)
                historia('que contam um pouco da história da masmorra.', 40, 175)
                pygame.display.update()
                time.sleep(8.5)
                capitulo_3a()
            elif action3 == 'ignorar':
                game_display.fill(b_grey)
                historia('VOCÊ MORREU!', 335, 290)
                pygame.display.update()
                time.sleep(3)
                game_introducao()
    else:
        pygame.draw.rect(game_display, ic3, (x3, y3, w3, h3))

    small_text = pygame.font.Font('freesansbold.ttf', 20)
    text_surface, text_rectangle = text_objects(msg3, small_text)
    text_rectangle.center = (x3 + (w3 / 2), y3 + (h3 / 3))
    game_display.blit(text_surface, text_rectangle)

def capitulo_2():
    cap_2 = True
    while cap_2:

        game_display.fill(b_grey)
        game_display.blit(bg_2, (0, 0))
        game_display.blit(img_heroi, (140, 420))
        game_display.blit(img_dragao, (480, 360))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        small_text = pygame.font.Font('freesansbold.ttf', 20)
        text_surface, text_rectangle = text_objects('', small_text)
        text_rectangle.center = ((display_width / 2), (display_height / 2))
        game_display.blit(text_surface, text_rectangle)

        button_3('LUTAR', 100, 50, 100, 50, b_grey, white, 'lutar')
        button_3('CONVERSAR', 320, 50, 140, 50, b_blue, blue, 'conversar')
        button_3('IGNORAR', 550, 50, 100, 50, red, b_red, 'ignorar')

        pygame.display.update()
        clock.tick(60)

def button_4(msg4, x4, y4, w4, h4, ic4, ac4, action4 = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x4 + w4 > mouse[0] > x4 and y4 + h4 > mouse[1] > y4:
        pygame.draw.rect(game_display, ac4, (x4, y4, w4, h4))
        if click[0] == 1 and action4 != None:
            if action4 == 'conversar':
                game_display.fill(b_grey)
                historia('A aventureira explica que as criaturas dropam', 40, 100)
                historia('itens valiosos. E o mostrará o caminho para seguir.', 40, 125)
                pygame.display.update()
                time.sleep(5)
                capitulo_3b()
            elif action4 == 'matar':
                game_display.fill(b_grey)
                historia('A aventureira joga um veneno mortal no herói para se salvar!', 40, 100)
                historia('VOCÊ MORREU!', 40, 175)
                pygame.display.update()
                time.sleep(5)
                game_introducao()
    else:
        pygame.draw.rect(game_display, ic4, (x4, y4, w4, h4))

    small_text = pygame.font.Font('freesansbold.ttf', 20)
    text_surface, text_rectangle = text_objects(msg4, small_text)
    text_rectangle.center = (x4 + (w4 / 2), y4 + (h4 / 2))
    game_display.blit(text_surface, text_rectangle)

def capitulo_3a():
    cap_3a = True
    while cap_3a:

        game_display.fill(b_grey)
        game_display.blit(bg_2, (0, 0))
        game_display.blit(img_heroi, (140, 420))
        game_display.blit(img_ninja, (480, 420))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        small_text = pygame.font.Font('freesansbold.ttf', 20)
        text_surface, text_rectangle = text_objects('', small_text)
        text_rectangle.center = ((display_width / 2), (display_height / 2))
        game_display.blit(text_surface, text_rectangle)

        button_4('CONVERSAR', 150, 50, 140, 50, b_grey, white, 'conversar')
        button_4('MATÁ-LA', 550, 50, 100, 50, red, b_red, 'matar')

        pygame.display.update()
        clock.tick(60)

def button_5(msg5, x5, y5, w5, h5, ic5, ac5, action5 = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x5 + w5 > mouse[0] > x5 and y5 + h5 > mouse[1] > y5:
        pygame.draw.rect(game_display, ac5, (x5, y5, w5, h5))
        if click[0] == 1 and action5 != None:
            if action5 == 'explorar':
                game_display.fill(b_grey)
                historia('Você encontrou um pergaminho!', 40, 100)
                historia('"Ainda é um mistério sobre como a masmorra surgiu.', 40, 125)
                historia('Há suspeitas de que um grande mago a criou,', 40, 150)
                historia('mas sem grandes evidências. Será outra dimensão?', 40, 175)
                historia('Há monstros que não atacam humanos a qualquer momento,', 40, 200)
                historia('há monstros extremamente nocivos, há humanos...', 40, 225)
                historia('Há tudo na masmorra, exceto a verdade sobre sua origem."', 40, 250)
                pygame.display.update()
                time.sleep(16)
                game_display.fill(b_grey)
                historia('Ainda no segundo andar, o herói nota que o local está', 40, 100)
                historia('cheirando sangue e encontra o guardião do andar.', 40, 125)
                pygame.display.update()
                time.sleep(5.5)
                capitulo_4()
            elif action5 == 'avancar':
                game_display.fill(b_grey)
                pygame.display.update()
                time.sleep(1)
                capitulo_4()
    else:
        pygame.draw.rect(game_display, ic5, (x5, y5, w5, h5))

    small_text = pygame.font.Font('freesansbold.ttf', 20)
    text_surface, text_rectangle = text_objects(msg5, small_text)
    text_rectangle.center = (x5 + (w5 / 2), y5 + (h5 / 2))
    game_display.blit(text_surface, text_rectangle)

def capitulo_3b():
    cap_3b = True
    while cap_3b:

        game_display.fill(b_grey)
        game_display.blit(bg_2, (0, 0))
        game_display.blit(img_heroi, (140, 420))
        game_display.blit(img_ninja, (220, 420))
        game_display.blit(img_pergaminho_1, (540, 420))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        small_text = pygame.font.Font('freesansbold.ttf', 20)
        text_surface, text_rectangle = text_objects('', small_text)
        text_rectangle.center = ((display_width / 2), (display_height / 2))
        game_display.blit(text_surface, text_rectangle)

        button_5('EXPLORAR', 150, 50, 140, 50, b_grey, white, 'explorar')
        button_5('AVANÇAR', 550, 50, 125, 50, red, b_red, 'avancar')

        pygame.display.update()
        clock.tick(60)

def button_6(msg6, x6, y6, w6, h6, ic6, ac6, action6 = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x6 + w6 > mouse[0] > x6 and y6 + h6 > mouse[1] > y6:
        pygame.draw.rect(game_display, ac6, (x6, y6, w6, h6))
        if click[0] == 1 and action6 != None:
            if action6 == 'lutar':
                game_display.fill(b_grey)
                historia('O herói empunha sua espada dourada e avança', 40, 100)
                historia('rumo ao monstro! O monstro resiste aos cortes', 40, 125)
                historia('profundos do herói e tenta acertá-lo com um', 40, 150)
                historia('golpe flamejante, mas o herói se esquiva e', 40, 175)
                historia('acerta um golpe fatal no monstro!', 40, 200)
                pygame.display.update()
                time.sleep(12)
                game_display.fill(b_grey)
                historia('A aventureira lembra-se que há um sábio', 40, 100)
                historia('vivendo no segundo andar e vocês se unem', 40, 125)
                historia('para buscá-lo. O herói se questiona sobre', 40, 150)
                historia('a possibilidade do sábio saber suas memórias', 40, 175)
                historia('perdidas e ajudá-lo a recuperá-las.', 40, 200)
                pygame.display.update()
                time.sleep(12)
                capitulo_5a()
            elif action6 == 'correr':
                game_display.fill(b_grey)
                historia('Você observa o monstro paralisado e corre rumo à saída.', 40, 100)
                historia('O monstro voa e o golpeia com suas garras! Era uma armadilha!', 40, 125)
                historia('VOCÊ MORREU!', 40, 200)
                pygame.display.update()
                time.sleep(7)
                game_introducao()
    else:
        pygame.draw.rect(game_display, ic6, (x6, y6, w6, h6))

    small_text = pygame.font.Font('freesansbold.ttf', 20)
    text_surface, text_rectangle = text_objects(msg6, small_text)
    text_rectangle.center = (x6 + (w6 / 2), y6 + (h6 / 2))
    game_display.blit(text_surface, text_rectangle)

def capitulo_4():
    cap_4 = True
    while cap_4:

        game_display.fill(b_grey)
        game_display.blit(bg_2, (0, 0))
        game_display.blit(img_heroi, (140, 420))
        game_display.blit(img_ninja, (220, 420))
        game_display.blit(img_monstro, (480, 420))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        small_text = pygame.font.Font('freesansbold.ttf', 20)
        text_surface, text_rectangle = text_objects('', small_text)
        text_rectangle.center = ((display_width / 2), (display_height / 2))
        game_display.blit(text_surface, text_rectangle)

        button_6('LUTAR', 150, 50, 100, 50, b_grey, white, 'lutar')
        button_6('CORRER', 550, 50, 100, 50, red, b_red, 'correr')

        pygame.display.update()
        clock.tick(60)

def button_7(msg7, x7, y7, w7, h7, ic7, ac7, action7 = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x7 + w7 > mouse[0] > x7 and y7 + h7 > mouse[1] > y7:
        pygame.draw.rect(game_display, ac7, (x7, y7, w7, h7))
        if click[0] == 1 and action7 != None:
            if action7 == 'conversar':
                game_display.fill(b_grey)
                historia('O sábio identifica que o herói está amaldiçoado', 40, 100)
                historia('e explica ao herói o que é a maldição,', 40, 125)
                historia('dizendo ao herói como a maldição pode ser purificada.', 40, 150)
                pygame.display.update()
                time.sleep(1)
                capitulo_5b()
            elif action7 == 'atacar':
                game_display.fill(b_grey)
                historia('O herói suspeita do sábio assim que o vê e', 40, 100)
                historia('empunha sua espada. Sem permitir que o sábio', 40, 125)
                historia('reagisse, o herói apunhala o sábio no peito.', 40, 150)
                historia('Um pergaminho cai no chão e o herói o pega.', 40, 175)
                pygame.display.update()
                time.sleep(10)
                game_display.fill(black)
                pygame.display.update()
                time.sleep(0.5)
                game_display.fill(b_grey)
                historia('Herói diz ofegante:', 40, 100)
                historia('Eu... Eu... Eu me lembrei!', 40, 125)
                historia('Meu amigo... Por quê? [...]', 40, 150)
                pygame.display.update()
                time.sleep(7)
                game_display.fill(b_grey)
                historia('Após descobrir sobre suas memórias, o herói avança para', 40, 100)
                historia('o terceiro andar e vê à sua frente um gigante sentado em um trono.', 40, 125)
                historia('Atrás dele há uma porta enorme!', 40, 150)
                pygame.display.update()
                time.sleep(8)
                capitulo_6()
    else:
        pygame.draw.rect(game_display, ic7, (x7, y7, w7, h7))

    small_text = pygame.font.Font('freesansbold.ttf', 20)
    text_surface, text_rectangle = text_objects(msg7, small_text)
    text_rectangle.center = (x7 + (w7 / 2), y7 + (h7 / 2))
    game_display.blit(text_surface, text_rectangle)

def capitulo_5a():
    cap_5a = True
    while cap_5a:

        game_display.fill(b_grey)
        game_display.blit(bg_2, (0, 0))
        game_display.blit(img_heroi, (140, 420))
        game_display.blit(img_ninja, (220, 420))
        game_display.blit(img_sabio, (480, 420))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        small_text = pygame.font.Font('freesansbold.ttf', 20)
        text_surface, text_rectangle = text_objects('', small_text)
        text_rectangle.center = ((display_width / 2), (display_height / 2))
        game_display.blit(text_surface, text_rectangle)

        button_7('CONVERSAR', 150, 50, 140, 50, b_grey, white, 'conversar')
        button_7('ATACAR', 550, 50, 120, 50, red, b_red, 'atacar')

        pygame.display.update()
        clock.tick(60)

def button_8(msg8, x8, y8, w8, h8, ic8, ac8, action8 = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x8 + w8 > mouse[0] > x8 and y8 + h8 > mouse[1] > y8:
        pygame.draw.rect(game_display, ac8, (x8, y8, w8, h8))
        if click[0] == 1 and action8 != None:
            if action8 == 'explorar':
                game_display.fill(b_grey)
                historia('O herói pega o pergaminho.', 40, 100)
                pygame.display.update()
                time.sleep(2.5)
                game_display.fill(black)
                pygame.display.update()
                time.sleep(0.5)
                game_display.fill(b_grey)
                historia('Herói diz ofegante:', 40, 100)
                historia('Eu... Eu... Eu me lembrei!', 40, 125)
                historia('Meu amigo... Por quê? [...]', 40, 150)
                pygame.display.update()
                time.sleep(7)
                game_display.fill(b_grey)
                historia('Após descobrir sobre suas memórias, o herói avança para', 40, 100)
                historia('o terceiro andar e vê à sua frente um gigante sentado em um trono.', 40, 125)
                historia('Atrás dele há uma porta enorme!', 40, 150)
                pygame.display.update()
                time.sleep(8)
                capitulo_6()
            elif action8 == 'andar':
                game_display.fill(b_grey)
                historia('O herói observa um pergaminho e sente', 40, 100)
                historia('que está o chamando.', 40, 125)
                historia('Explore o local!', 40, 150)
                pygame.display.update()
                time.sleep(7)
                capitulo_5b()

    else:
        pygame.draw.rect(game_display, ic8, (x8, y8, w8, h8))

    small_text = pygame.font.Font('freesansbold.ttf', 20)
    text_surface, text_rectangle = text_objects(msg8, small_text)
    text_rectangle.center = (x8 + (w8 / 2), y8 + (h8 / 2))
    game_display.blit(text_surface, text_rectangle)

def capitulo_5b():
    cap_5b = True
    while cap_5b:

        game_display.fill(b_grey)
        game_display.blit(bg_2, (0, 0))
        game_display.blit(img_heroi, (140, 420))
        game_display.blit(img_ninja, (220, 420))
        game_display.blit(img_pergaminho_2, (540, 420))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        small_text = pygame.font.Font('freesansbold.ttf', 20)
        text_surface, text_rectangle = text_objects('', small_text)
        text_rectangle.center = ((display_width / 2), (display_height / 2))
        game_display.blit(text_surface, text_rectangle)

        button_8('EXPLORAR', 150, 50, 140, 50, b_grey, white, 'explorar')
        button_8('ANDAR', 550, 50, 100, 50, red, b_red, 'andar')

        pygame.display.update()
        clock.tick(60)

def button_9(msg9, x9, y9, w9, h9, ic9, ac9, action9 = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x9 + w9 > mouse[0] > x9 and y9 + h9 > mouse[1] > y9:
        pygame.draw.rect(game_display, ac9, (x9, y9, w9, h9))
        if click[0] == 1 and action9 != None:
            if action9 == 'lutar':
                game_display.fill(b_grey)
                historia('O herói dá a chance ao gigante de deixá-lo passar,', 40, 100)
                historia('mas o gigante sorri e avança com seu machado,', 40, 125)
                historia('O herói ergue sua espada e a chama pelo nome:', 40, 150)
                historia('E X C A L I B U R !', 40, 175)
                historia('Com um golpe nunca visto o herói aniquila o gigante!', 40, 200)
                historia('Ofegante, o herói caminha até a porta.', 40, 225)
                pygame.display.update()
                time.sleep(13)
                capitulo_6a()
            elif action9 == 'fugir':
                game_display.fill(b_grey)
                historia('O herói tenta correr do gigante,', 40, 100)
                historia('mas o gigante direciona seu machado para o herói.', 40, 125)
                historia('Não há mais volta, você terá de enfrentar o gigante.', 40, 150)
                pygame.display.update()
                time.sleep(7)
                capitulo_6()

    else:
        pygame.draw.rect(game_display, ic9, (x9, y9, w9, h9))

    small_text = pygame.font.Font('freesansbold.ttf', 20)
    text_surface, text_rectangle = text_objects(msg9, small_text)
    text_rectangle.center = (x9 + (w9 / 2), y9 + (h9 / 2))
    game_display.blit(text_surface, text_rectangle)

def capitulo_6():
    cap_6 = True
    while cap_6:

        game_display.fill(b_grey)
        game_display.blit(bg_3, (0, 0))
        game_display.blit(img_heroi, (110, 420))
        game_display.blit(img_giant, (400, 360))
        game_display.blit(img_pergaminho_1, (720, 420))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        small_text = pygame.font.Font('freesansbold.ttf', 20)
        text_surface, text_rectangle = text_objects('', small_text)
        text_rectangle.center = ((display_width / 2), (display_height / 2))
        game_display.blit(text_surface, text_rectangle)

        button_9('LUTAR', 150, 50, 100, 50, b_grey, white, 'lutar')
        button_9('FUGIR', 550, 50, 100, 50, red, b_red, 'fugir')

        pygame.display.update()
        clock.tick(60)

def button_10(msg10, x10, y10, w10, h10, ic10, ac10, action10 = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x10 + w10 > mouse[0] > x10 and y10 + h10 > mouse[1] > y10:
        pygame.draw.rect(game_display, ac10, (x10, y10, w10, h10))
        if click[0] == 1 and action10 != None:
            if action10 == 'explorar':
                game_display.fill(b_grey)
                historia('O herói encontra um pergaminho e o lê.', 40, 100)
                historia('"A masmorra vem do mais puro ódio cultivado', 40, 125)
                historia('pelo homem em nome da inveja e sede de poder."', 40, 150)
                pygame.display.update()
                time.sleep(7)
                game_display.fill(b_grey)
                historia('O herói abre a porta e encontra seu amigo do outro lado.', 40, 100)
                historia('Herói: O que você está fazendo aqui?', 40, 125)
                historia('Amigo: Hahahaha! Finalmente chegou!', 40, 150)
                historia('Herói: O quê? Como assim? […] O que isso quer dizer?', 40, 175)
                historia('Amigo: Eu planejei tudo por cem anos! Criei esta masmorra,', 40, 200)
                historia('fiz você perder suas memórias e todas pessoas esqueceram quem é você!', 40, 225)
                historia('Herói furioso: Por que você fez isso?', 40, 250)
                historia('Amigo: Nunca gostei de você e chegou a hora de pôr um fim nisso!', 40, 275)
                historia('Mostre como um verdadeiro herói age:', 40, 350)
                historia('Mate o traidor ou perdoe-o mostrando a bondade em seu coração.', 40, 375)
                pygame.display.update()
                time.sleep(24)
                capitulo_7()
            elif action10 == 'avancar':
                game_display.fill(b_grey)
                historia('O herói abre a porta e encontra seu amigo do outro lado.', 40, 100)
                historia('Herói: O que você está fazendo aqui?', 40, 125)
                historia('Amigo: Hahahaha! Finalmente chegou!', 40, 150)
                historia('Herói: O quê? Como assim? […] O que isso quer dizer?', 40, 175)
                historia('Amigo: Eu planejei tudo por cem anos! Criei esta masmorra,', 40, 200)
                historia('fiz você perder suas memórias e todas pessoas esqueceram quem é você!', 40, 225)
                historia('Herói furioso: Por que você fez isso?', 40, 250)
                historia('Amigo: Nunca gostei de você e chegou a hora de pôr um fim nisso!', 40, 275)
                historia('Mostre como um verdadeiro herói age:', 40, 350)
                historia('Mate o traidor ou perdoe-o mostrando a bondade em seu coração.', 40, 375)
                pygame.display.update()
                time.sleep(25)
                capitulo_7()

    else:
        pygame.draw.rect(game_display, ic10, (x10, y10, w10, h10))

    small_text = pygame.font.Font('freesansbold.ttf', 20)
    text_surface, text_rectangle = text_objects(msg10, small_text)
    text_rectangle.center = (x10 + (w10 / 2), y10 + (h10 / 2))
    game_display.blit(text_surface, text_rectangle)

def capitulo_6a():
    cap_6a = True
    while cap_6a:

        game_display.fill(b_grey)
        game_display.blit(bg_3, (0, 0))
        game_display.blit(img_heroi, (450, 420))
        game_display.blit(img_pergaminho_1, (720, 420))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        small_text = pygame.font.Font('freesansbold.ttf', 20)
        text_surface, text_rectangle = text_objects('', small_text)
        text_rectangle.center = ((display_width / 2), (display_height / 2))
        game_display.blit(text_surface, text_rectangle)

        button_10('EXPLORAR', 150, 50, 140, 50, b_grey, white, 'explorar')
        button_10('AVANÇAR', 550, 50, 140, 50, blue, b_blue, 'avancar')

        pygame.display.update()
        clock.tick(60)

def button_11(msg11, x11, y11, w11, h11, ic11, ac11, action11 = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x11 + w11 > mouse[0] > x11 and y11 + h11 > mouse[1] > y11:
        pygame.draw.rect(game_display, ac11, (x11, y11, w11, h11))
        if click[0] == 1 and action11 != None:
            if action11 == 'lutar':
                game_display.fill(b_grey)
                historia('O herói e seu amigo travam uma batalha feroz.', 40, 100)
                historia('Em seus últimos suspiros o traidor lança um feitiço para matá-lo,', 40, 125)
                historia('mas a espada drena toda sua energia vital,', 40, 150)
                historia('e assim se torna a maior relíquia de poder da masmorra.', 40, 175)
                historia('Todos no reino sentem o poder da espada e', 40, 200)
                historia('cria-se a lenda de que quem empunhar espada', 40, 225)
                historia('será o guerreiro mais poderoso.', 40, 250)
                historia('F I M !', 40, 325)
                pygame.display.update()
                time.sleep(35)
                game_introducao()
            elif action11 == 'perdoar':
                game_display.fill(b_grey)
                historia('O herói perdoa seu amigo pelas coisas que fez,', 40, 100)
                historia('mas o amigo ainda mantém todo o rancor pelo herói e,', 40, 125)
                historia('aproveitando da bondade e guarda baixa do herói,', 40, 150)
                historia('lança um feitiço que drena a vida do herói.', 40, 175)
                historia('No entanto, a espada do herói não permite que o amigo absorva', 40, 200)
                historia('para si as forças vitais do herói e drena para a própria espada.', 40, 225)
                historia('Desta forma, a espada torna-se a maior relíquia de poder da masmorra.', 40, 250)
                historia('Todos no reino sentem o poder da espada e cria-se a lenda', 40, 275)
                historia('de que quem empunhar espada será o guerreiro mais poderoso.', 40, 300)
                historia('O amigo fica enlouquecido com a própria falha e', 40, 325)
                historia('ficará eternamente preso na própria masmorra.', 40, 350)
                historia('F I M !', 40, 425)
                pygame.display.update()
                time.sleep(45)
                game_introducao()
    else:
        pygame.draw.rect(game_display, ic11, (x11, y11, w11, h11))

    small_text = pygame.font.Font('freesansbold.ttf', 20)
    text_surface, text_rectangle = text_objects(msg11, small_text)
    text_rectangle.center = (x11 + (w11 / 2), y11 + (h11 / 2))
    game_display.blit(text_surface, text_rectangle)

def capitulo_7():
    cap_7 = True
    while cap_7:

        game_display.fill(b_grey)
        game_display.blit(bg_3, (0, 0))
        game_display.blit(img_heroi, (450, 420))
        game_display.blit(img_amigo, (530, 420))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        small_text = pygame.font.Font('freesansbold.ttf', 20)
        text_surface, text_rectangle = text_objects('', small_text)
        text_rectangle.center = ((display_width / 2), (display_height / 2))
        game_display.blit(text_surface, text_rectangle)

        button_11('LUTAR', 150, 50, 100, 50, b_grey, white, 'lutar')
        button_11('PERDOAR', 550, 50, 100, 50, blue, b_blue, 'perdoar')

        pygame.display.update()
        clock.tick(60)

game_introducao()
pygame.quit()
quit()