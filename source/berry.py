import pygame
from gameConstants import Color
from gameConstants import Dimensions
from gameConstants import Fonts


class Berry(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, 10, 10)
