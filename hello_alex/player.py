import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 200, 0)
BRIGHT_GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WIDTH = 800
HEIGHT = 600
pygame.font.init()
BASICFONT = pygame.font.SysFont(None, 50)
SMALLFONT = pygame.font.SysFont(None, 25)


class Player:
    def __init__(self, x=50, y=450):
        self.x = x
        self.y = y
        self.events = []
        self.pressed = None

    def update(self, events):
        self.events = events

    def move(self, direction):
        if direction == 'left' and self.x >= 10:
            self.x -= 10
        elif direction == 'right' and self.x < 780:
            self.x += 10

    def refresh(self, events):
        self.update(events)
