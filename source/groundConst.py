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
        [[(200, h), (350, h), (500, h)], [(3,150,300), (4,40), (2,350), (5 ,550)]],
        [[(100, h), (175, h), (300, h), (550, h), (250, h)], [(4,50), (6,100), (5,150), (3,200), (4,250)]],
        [[(100, h), (200, h), (300, h), (400, h), (500, h)],
         [(5,75), (4,150), (5,225), (3,375), (9, 425), (7,525)]],
        [[(70, h), (140, h), (210, h), (280, h), (350, h), (420, h), (490, h), (560, h)],
         [(3,240), (7,280), (5, 300), (8, 350), (4,380)]],
        [[(60, h), (190, h), (230, h), (430, h), (520, h), (540, h)],
         [(4, 90), (5,160), (5, 200), (3,270), (4, 340), (2, 430)]]
    ]

# levelOne = [ground0, ground1]
