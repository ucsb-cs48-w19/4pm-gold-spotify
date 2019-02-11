import pygame

class Berry(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.Surface([x, y], pygame.SRCALPHA)
        self.image = pygame.image.load("berry.png").convert_alpha()
        self.rect = pygame.Rect(self.x,self.y,60,60)

    def erase(self):
        self.image = self.image.convert()
        self.image.set_alpha(0)
        self.kill()
