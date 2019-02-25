from enum import Enum
import pygame

pygame.init()
pygame.font.init()


class Color(Enum):
	BLACK = (0,0,0)
	WHITE = (255, 255, 255)
	RED = (255, 0, 0)
	GREEN = (0,200,0)
	BRIGHT_GREEN = (0,255,0)
	BLUE = (0,0,255)


class Dimensions(Enum):
	WIDTH = 800
	HEIGHT = 600


class Fonts(Enum):
	BASICFONT = pygame.font.SysFont(None, 50)
	SMALLFONT = pygame.font.SysFont(None, 25)

class Sounds(Enum):
	SpiderSqueak = "spiderSqueak.wav"
