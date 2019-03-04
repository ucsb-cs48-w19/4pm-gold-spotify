import pygame
from gameConstants import BerryConst

class Berry(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, BerryConst.WIDTH.value, BerryConst.HEIGHT.value)
