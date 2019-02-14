# groundData.py
from enum import Enum
import pygame
from gameConstants import Dimensions

pygame.init()
pygame.font.init()

# levelOne object will hold info about the spiders/berries in each ground block. Each index in levelOne
# corresponds to a ground object

# syntax: [berries(x,y), spiders(x, speed)]
h = (4 / 5) * Dimensions.HEIGHT.value


class LevelOne(Enum):
    g = [
        [[(200, h), (350, h), (500, h)], [(150, 1), (40, 2), (350, 3), (550, 4)]],
        [[(100, h), (175, h), (300, h), (550, h), (250, h)], [(50, 5), (100, 1), (150, 2), (200, 3), (250, 4)]],
        [[(100, h), (200, h), (300, h), (400, h), (500, h)],
         [(75, 5), (150, 4), (225, 2), (375, 3), (425, 1), (525, 5)]],
        [[(70, h), (140, h), (210, h), (280, h), (350, h), (420, h), (490, h), (560, h)],
         [(240, 2), (280, 3), (300, 4), (350, 5), (380, 2)]],
        [[(60, h), (190, h), (230, h), (430, h), (520, h), (540, h)],
         [(90, 4), (160, 5), (200, 3), (270, 1), (340, 4), (430, 2)]]
    ]

# levelOne = [ground0, ground1]
