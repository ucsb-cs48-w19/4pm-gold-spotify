# groundData.py
from enum import Enum
import pygame

pygame.init()
pygame.font.init()


# levelOne object will hold info about the spiders/berries in each ground block. Each index in levelOne
# corresponds to a ground object

# syntax: [berries(x,y), spiders(x, speed)]

class LevelOne(Enum):
    g = [
         [[(50, 100), (100, 100), (150, 100)], [(200, 3), (250, 5), (300, 7), (350, 10)]],
         [[(50, 50), (100, 50), (150, 50), (200, 50), (250, 50)], [(50, 1), (100, 2), (150, 3), (200, 4), (250, 5)]]
    ]

# levelOne = [ground0, ground1]
