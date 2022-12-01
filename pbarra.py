import pygame
PRETO = (0,0,0)

#cria a classe barra 
class Barra(pygame.sprite.Sprite):

 
    def __init__(self, color, width, height):
        super().__init__()
 
        # altura e largura da barra
        self.image = pygame.Surface([width, height])
        self.image.fill(PRETO)
        self.image.set_colorkey(PRETO)
 
        # Desenha a barra
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()

    def moveesquerda(self, pixels):
        self.rect.x -= pixels
	    #Não permite passar dos limites da tela
        if self.rect.x < 0:
          self.rect.x = 0
 
    def movedireita(self, pixels):
        self.rect.x += pixels
        #Não permite passar dos limites da tela
        if self.rect.x > 700:
          self.rect.x = 700