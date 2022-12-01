#Import pygame
import pygame
#import das classes bola, bloco, barra
from pbarra import Barra
from pbola import Bola
from pbloco import Bloco
 
pygame.init()
 
# Define as cores
BRANCO = (255,255,255)
AZULESCURO = (36,90,190)
AZULCLARO = (0,176,240)
VERMELHO = (255,0,0)
LARANJA = (255,100,0)
AMARELO = (255,255,0)
 
pontos = 0
vidas = 3
 
# Abre nova janela
tamanho = (800, 600)
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("bloco Break")
 
#Lista com todos os sprites
lista_todos_sprites = pygame.sprite.Group()
 
#Cria a barra
barra = Barra(AZULCLARO, 100, 10)
barra.rect.x = 350
barra.rect.y = 560
 
#Cria a bola
bola = Bola(BRANCO,10,10)
bola.rect.x = 345
bola.rect.y = 195

todos_blocos = pygame.sprite.Group()
for i in range(7):
    bloco = Bloco(VERMELHO,80,30)
    bloco.rect.x = 60 + i* 100
    bloco.rect.y = 60
    lista_todos_sprites.add(bloco)
    todos_blocos.add(bloco)
for i in range(7):
    bloco = Bloco(LARANJA,80,30)
    bloco.rect.x = 60 + i* 100
    bloco.rect.y = 100
    lista_todos_sprites.add(bloco)
    todos_blocos.add(bloco)
for i in range(7):
    bloco = Bloco(AMARELO,80,30)
    bloco.rect.x = 60 + i* 100
    bloco.rect.y = 140
    lista_todos_sprites.add(bloco)
    todos_blocos.add(bloco)
 
# Adiciona a barra e a bola a lista de sprites
lista_todos_sprites.add(barra)
lista_todos_sprites.add(bola)
 

continuar  = True
 
# controla o quão rapido a tela atualiza
clock = pygame.time.Clock()
 
# Loop principal
while continuar :
    # Evento principal
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
              continuar  = False 
 
    #Mover a barra quando o usuario aperta seta esquerda ou direita
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        barra.moveesquerda(5)
    if teclas[pygame.K_RIGHT]:
        barra.movedireita(5)
 
    
    lista_todos_sprites.update()
 
    #Checa se a bola está rebatendo em uma das 4 paredes
    if bola.rect.x>=790:
        bola.velocidade[0] = -bola.velocidade[0]
    if bola.rect.x<=0:
        bola.velocidade[0] = -bola.velocidade[0]
    if bola.rect.y>590:
        bola.velocidade[1] = -bola.velocidade[1]
        vidas -= 1
        if vidas == 0:
            #Mostrar mensagem fim de jogo por 3 segundos
            fonte = pygame.font.Font(None, 74)
            texto = fonte.render("Fim de Jogo", 1, BRANCO)
            tela.blit(texto, (250,300))
            pygame.display.flip()
            pygame.time.wait(3000)
 
            #Pare o jogo
            continuar = False
 
    if bola.rect.y<40:
        bola.velocidade[1] = -bola.velocidade[1]
 
    #Detecta colisões
    if pygame.sprite.collide_mask(bola, barra):
      bola.rect.x -= bola.velocidade[0]
      bola.rect.y -= bola.velocidade[1]
      bola.bounce()
 
    #Checa se a bola colidiu com algum dos blocos
    lista_col_blocos = pygame.sprite.spritecollide(bola,todos_blocos,False)
    for bloco in lista_col_blocos:
      bola.bounce()
      pontos += 1
      bloco.kill()
      if len(todos_blocos)==0:
            font = pygame.font.Font(None, 74)
            texto = font.render("LEVEL COMPLETE", 1, BRANCO)
            tela.blit(texto, (200,300))
            pygame.display.flip()
            pygame.time.wait(3000)
 
            #Para o jogo
            continuar =False
 

    # Preenche a tela com azul escuro
    tela.fill(AZULESCURO)
    pygame.draw.line(tela, BRANCO, [0, 38], [800, 38], 2)
 
    #Mostra o numero de pontos e vidas no topo da tela
    font = pygame.font.Font(None, 34)
    texto = font.render("pontos: " + str(pontos), 1, BRANCO)
    tela.blit(texto, (20,10))
    texto = font.render("vidas: " + str(vidas), 1, BRANCO)
    tela.blit(texto, (650,10))
 
    #desenha os sprites
    lista_todos_sprites.draw(tela)
 

    pygame.display.flip()
 
    #Limita a 60 frames
    clock.tick(60)
 
#Para a Engine
pygame.quit()