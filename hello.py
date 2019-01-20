import pygame
import time
#from pygame.locals import *
pygame.init()

BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)

#https://stackoverflow.com/questions/19954469/how-to-get-the-resolution-of-a-monitor-in-pygame
# a few different options for making a full screen
#gameDisplay = pygame.display.set_mode((2000, 1000)) (hardcoded to Jasus dimensions)
#gameDisplay = pygame.display.set_mode((0,0), pygame.FULLSCREEN) (this one's weird)
# the one below is pretty good
infoObject = pygame.display.Info()
gameDisplay = pygame.display.set_mode((infoObject.current_w, infoObject.current_h))
pygame.display.set_caption("My First Game")

clock = pygame.time.Clock()

def textObjects(text, font):
	textSurface = font.render(text, True, WHITE)
	return textSurface, textSurface.get_rect()

def showMessage(text):
	largeText = pygame.font.Font('freesansbold.ttf', 115)
	TextSurf, TextRect = textObjects(text, largeText)
	TextRect.center = ((800), (1000/2))
	gameDisplay.blit(TextSurf, TextRect)
	pygame.display.update()
	time.sleep(20)
def mainGame():
	showMessage("Hello World!")
	pygame.quit()
mainGame()
