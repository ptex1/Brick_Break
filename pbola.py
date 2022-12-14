import pygame
from random import randint
 
PRETO = (0, 0, 0)

#cria a classe bola
class Bola(pygame.sprite.Sprite):
    
    def __init__(self, color, width, height):
        super().__init__()
        
        # altura e largura da "bola"
        self.image = pygame.Surface([width, height])
        self.image.fill(PRETO)
        self.image.set_colorkey(PRETO)
 
        # Desenha a nossa bola retangular
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        #define a velocidade
        self.velocidade = [randint(3,5),randint(-6,6)]
        
        self.rect = self.image.get_rect()
    
    def update(self):
        self.rect.x += self.velocidade[0]
        self.rect.y += self.velocidade[1]
          
    def bounce(self):
        self.velocidade[0] = -self.velocidade[0]
        self.velocidade[1] = randint(-6,6)
        while self.velocidade[1] == 0:
            self.velocidade[1] = randint(-8,8)