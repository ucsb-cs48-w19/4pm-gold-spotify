import pygame
from gameConstants import Color
from gameConstants import Dimensions
from gameConstants import Fonts


class Spider(pygame.sprite.Sprite):
    # placeholder for spiders
    def __init__(self, x, speed):
        super().__init__()
        self.rect = pygame.Rect(x, 100, 30, 30)
        self.speed = speed

    # def draw(self):
    #     pygame.draw.rect(gameDisplay, Color.GREEN.value, self.rect)
