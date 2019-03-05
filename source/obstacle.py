import pygame
from gameConstants import Color
from gameConstants import Dimensions
from gameConstants import Fonts

class Obstacle(pygame.sprite.Sprite):
	def __init__(self,x,y,w,h):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((w,h))
		self.image.fill(Color.BLACK.value)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
