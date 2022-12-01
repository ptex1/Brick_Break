import pygame
PRETO = (0,0,0)

#cria a classe bloco
class Bloco(pygame.sprite.Sprite):


    def __init__(self, color, width, height):
        super().__init__()

        # altura e largura do bloco
        self.image = pygame.Surface([width, height])
        self.image.fill(PRETO)
        self.image.set_colorkey(PRETO)

        #Desenha o bloco
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()