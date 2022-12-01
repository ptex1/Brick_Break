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