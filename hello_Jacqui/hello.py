import pygame
import time
from pygame.locals import *
pygame.init()

BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)
ORANGE = (255,140,0)
PURPLE = (128, 0, 128)

allText = pygame.sprite.Group()
allButtons = pygame.sprite.Group()
allSprites = pygame.sprite.Group()

#https://stackoverflow.com/questions/19954469/how-to-get-the-resolution-of-a-monitor-in-pygame
# a few different options for making a full screen
#gameDisplay = pygame.display.set_mode((2000, 1000)) (hardcoded to Jasus dimensions)
#gameDisplay = pygame.display.set_mode((0,0), pygame.FULLSCREEN) (this one's weird)
# the one below is pretty good
infoObject = pygame.display.Info()
gameDisplay = pygame.display.set_mode((infoObject.current_w, infoObject.current_h))
pygame.display.set_caption("My First Game")

clock = pygame.time.Clock()
#bg = pygame.image.load("bgtest.png")
#bgRect = bg.get_rect()

class TextSprite(pygame.sprite.Sprite):
	def __init__(self,text, color, centerx, centery, font=pygame.font.Font('freesansbold.ttf',115)):
		super().__init__()
		if not pygame.font.get_init():
			pygame.font.init()
		self.textSurface = font.render(text, True, color)
		self.Rect = self.textSurface.get_rect()
		self.Rect.center = (centerx, centery)
#		largeText = pygame.font.Font('freesansbold.ttf', 115)
#		TextSurf, TextRect = textObjects(text, WHITE, largeText)
#		TextRect.center = ((800), (1000/2))
#		allSprites.add(self)
#		allButtons.add(self)
		gameDisplay.blit(self.textSurface, self.Rect)
		pygame.display.flip()
#		time.sleep(20)
	
class ButtonSprite(TextSprite):
	def __init__(self, text, orig, other, x,y, action=None):
#		super.__init__(text, BLACK, self.rect.centerx, self.rect.centery)
		self.action = action
		self.current = orig
		self.orig = orig
		self.other = other
		self.rect = pygame.Rect(x,y,100,50)
		super().__init__(text, BLACK, self.rect.centerx, self.rect.centery, pygame.font.Font('freesansbold.ttf',15))

#		self.t, self.tR = textObjects(text, BLACK)
#		self.tR.center = self.rect.center
#		TextSprite.__init__(self,text, BLACK, self.rect.centerx, self.rect.centery)
#		allButtons.add(self)
#		allSprites.add(self)
	def drawButton(self):
		pygame.draw.rect(gameDisplay, self.current, self.rect)
#		gameDisplay.blit(self.t,self.tR)
		pygame.display.flip()
#	t, tR = textObjects(text, BLACK)
#	tR.center = rect.center
#	gameDisplay.blit(t,tR)
#	pygame.display.update()
	def dark(self):
		self.current = BLACK
		pygame.display.flip()
	def detectMouse(self):
		'''
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
		if self.rect.left<mouse[0]<self.rect.right and self.rect.top<mouse[1]<self.rect.bottom: 
			if(self.current == self.orig):
				self.current = self.other
			else:
			 	self.current = self.orig
			self.drawButton()
			pygame.display.update()
			if click[0]==1 and self.action != None:
#				if(self.action ==GameLoop):
#					GameLoop(False)
				self.action()
				clock.tick()
		'''
		handled = False
		if self.rect.collidepoint(pygame.mouse.get_pos()):
			if(self.current == self.orig):
				self.current = self.other
			else:
			 	self.current = self.orig
			self.drawButton()
			pygame.display.update()
			if  pygame.mouse.get_pressed()[0] and not handled:
			 	self.action()
			 	handled = pygame.mouse.get_pressed()[0]
			 	# check if change to pygame getevent?

#	def insertImg(self,imgName):
#		img = pygame.image.load(imgName)


def endGame():

	for sprite in allButtons.sprites():
		sprite.dark()
		sprite.kill()


	for sprite in allSprites.sprites():
		sprite.kill()
#	for sprite in allButtons.sprites():
#		sprite.dark()
#		sprite.kill()
	'''
	allSprites.remove(allButtons)
	allButtons.empty()
	'''
	print(allButtons)
	gameDisplay.fill(WHITE)
	pygame.display.flip()
	time.sleep(2)
	gameDisplay.fill(BLACK)
#	pygame.display.flip()
	end = TextSprite("GAME OVER", WHITE, 800, 500)
#	time.sleep(2)
	repeat = ButtonSprite("Play Again!", PURPLE, WHITE, 300, 450, sayHello)
	quit = ButtonSprite("Quit!", PURPLE, WHITE, 1200, 450, pygame.quit)
	allSprites.add(end)
	allSprites.add(repeat)
	allSprites.add(quit)
	allButtons.add(repeat)
	allButtons.add(quit)
	allText.add(end)
	print(allButtons)
#	for button in allButtons.sprites():
#		button.drawButton()
#		button.detectMouse()

def sayHello():
	print(allButtons)
	gameDisplay.fill(BLACK)

	for sprite in allButtons.sprites():
		sprite.dark()
		sprite.kill()

	for sprite in allSprites.sprites():
		sprite.kill()
	'''
	allSprites.remove(allButtons)
	allButtons.empty()
	'''
	gameDisplay.fill(BLACK)
	hello = TextSprite("Hello World!", WHITE, 800, 500)
#	time.sleep(2)
	x = ButtonSprite("HI!", GREEN, ORANGE, 750, 650, endGame)
#	y = ButtonSprite("BYE!", RED, ORANGE, 1200, 450, endGame)
	allSprites.add(hello, x)
	allButtons.add(x)
	allText.add(hello)
#	for button in allButtons.sprites():
#		button.drawButton()
#		button.detectMouse()



def GameLoop(gameOver):
	sayHello()
	while not gameOver:
#		showMessage("Hello World!")
#		x = button("HI!", GREEN, 300, 450, endGame)
#		y = button("BYE!", RED, 1200, 450, endGame)
#		x.drawButton()
#		y.drawButton()
		for button in allButtons.sprites():
			button.drawButton()
			button.detectMouse()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameOver = True
#		x.detectMouse()
#		y.detectMouse()
		clock.tick()
#	gameDisplay.blit(bg, bgRect)
#	pygame.display.update()

def mainGame():
#background insertion line should go here later
	gameOver = False
	GameLoop(gameOver)
#	gameDisplay.blit(bg, bgRect)
	pygame.quit()
mainGame()
