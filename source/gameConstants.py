from enum import Enum
import pygame
from pygame.locals import *

pygame.font.init()
pygame.display.init()
infoObject = pygame.display.Info()

class Color(Enum):
	BLACK = (0,0,0)
	WHITE = (255, 255, 255)
	RED = (175, 39, 29)
	GREEN = (57, 160, 85)
	BRIGHT_GREEN = (70, 206, 107)
	BRIGHT_RED = (224, 48, 35)


class Dimensions(Enum):
#	WIDTH = 800
#	HEIGHT = 600
	WIDTH = infoObject.current_w
	HEIGHT = infoObject.current_h

class Fonts(Enum):
	BASICFONT = pygame.font.SysFont(None, 50)
	SMALLFONT = pygame.font.SysFont(None, 25)

class PlayerConst(Enum):
	SPEED = 8
	JUMP_V = 10
	MASS = 2
	HEALTH = 5
	WIDTH = 66
	HEIGHT = 110
	GROUND_DIST = 225
	PLAYER_FRAME = 6
	HEART_DIM = 30

class BerryConst(Enum):
	WIDTH = 10
	HEIGHT = 10

class SpiderConst(Enum):
	WIDTH = 35
	HEIGHT = 30
# class Sounds(Enum):
# 	SpiderSqueak = "spiderSqueak.wav"
