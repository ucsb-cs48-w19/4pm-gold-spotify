import pygame
import time
pygame.init()

BLACK = (0,0,0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

#create display window
#size = (2000, 1000)

bg= pygame.image.load("Untitled.png")
bgRect = bg.get_rect()

infoObj = pygame.display.Info()
#display = pygame.display.set_mode((infoObj.current_w, infoObj.current_h))
display = pygame.display.set_mode((bg.get_width(),bg.get_height()))
pygame.display.set_caption("Testing background")

clock = pygame.time.Clock()

def mainGame():
	display.blit(bg, bgRect)
	pygame.display.update()
	time.sleep(20)
mainGame()
