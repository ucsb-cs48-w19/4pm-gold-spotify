# groundData.py
from enum import Enum
import pygame
from gameConstants import Dimensions
pygame.init()
pygame.font.init()


# levelOne object will hold info about the spiders/berries in each ground block. Each index in levelOne
# corresponds to a ground object

# syntax: [berries(x,y), spiders(x, speed)]
h = (4/5)*Dimensions.HEIGHT.value

class LevelOne(Enum):
    g = [
 [ [(200, h), (350, h), (500, h) ] , [(150, 10), (400, 17), (350, 7), (550, 15)] ],
	[ [(100, h), (175, h), (300, h), (550, h), (250, h)], [(50, 50), (100, 10), (150, 17), (200, 20), (250, 40)]], 
         [ [(100, h), (200, h), (300, h), (400, h), (500, h) ], [ (75,50), (150,40), (225,20), (375,35), (425,10), (525,50) ] ],
	 [ [(70, h), (140, h), (210, h), (280, h), (350, h), (420, h), (490, h), (560, h) ], [ (240, 25), (280, 33), (300, 37), (350, 45), (380, 17) ] ],
	 [ [(60, h), (190, h), (230, h), (430, h), (520, h), (540, h) ], [(90, 37), (160, 50), (200, 30), (270, 10), (340, 43), (430, 26)] ]   
    ]

# levelOne = [ground0, ground1]
