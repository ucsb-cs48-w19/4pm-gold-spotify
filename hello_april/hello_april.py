#helloWorld.py
#MADE CHANGES2

import pygame
import time

#initiate pygame and all modules that come with it
pygame.init()


black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,200,0)
bright_green = (0,255,0)
bright_red = (255,69,0)

displayInfo = pygame.display.Info()
displayHeight = displayInfo.current_h//3
displayWidth = displayInfo.current_w//3
#next want to set up window/surface
gameDisplay = pygame.display.set_mode((displayWidth,displayHeight)) #width and height as a tuple
pygame.display.set_caption("Hello, World!")

#Next want to define the game's clock (frames/sec)
clock = pygame.time.Clock()

#sprite image
girlSprite = pygame.image.load('sprite.png').convert()
girlSprite= pygame.transform.scale(girlSprite, (displayWidth//10,displayHeight//8))
		
x = (displayWidth * 0.1)
y = (displayHeight * 0.8)


#Every game needs a game loop, the only thing that breaks out is a crash or a quit
#pygame grabs all events for you; pygame.event.get() gets any event that happened (move mouse, click)

#to update display: pygame.display.update()(can put parameters so that only
#certain things are updated; otherwise updates entire surface) OR
#pygame.display.flip() - always just updates the entire surface

#we want to define our frames per sec, how fast are we gonna do this stuff
clock.tick(60) #for parameter put the number of frames per second you want
             #if you want something to run fast but smooth then increase frames/sec
#gameDisplay.fill(white)  should come before any other image, or you wont see them

def girl(x,y):
    gameDisplay.blit(girlSprite,(x,y))    #image and location of image

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def displayMessageCenter(text, color):
    largeText = pygame.font.Font(None,115)
    TextSurf, TextRect = text_objects(text, largeText, color)
    TextRect.center = ((displayWidth/2),(displayHeight/2))
    gameDisplay.blit(TextSurf,TextRect)
    #pygame.display.update()

def displayMessageTest(text, color):
    largeText = pygame.font.Font(None,20)
    TextSurf, TextRect = text_objects(text, largeText, color)
    TextRect.center = ((displayWidth/2),(displayHeight*(3/4)))
    gameDisplay.blit(TextSurf,TextRect)
    #pygame.display.update()

    
class button:
    #(Display, color, Rect, message = "")
    def __init__(self, color, x, y, w, h, message = "" ):
        self.defaultColor = color
        self.x_pos = x
        self.y_pos = y
        self.width = w
        self.height = h
        self.message = message

    def displayMessage(self, Display, color = black):
        messageText = pygame.font.Font(None,50)
        textSurf = messageText.render(self.message, True, color)
        textRect = textSurf.get_rect()
        textRect.center = ( (self.x_pos +(self.width/2)), (self.y_pos+(self.height/2)) )
        Display.blit(textSurf, textRect)
        
    def drawB(self, Display):
        pygame.draw.rect(Display, self.defaultColor, (self.x_pos,self.y_pos,self.width,self.height) )
        self.displayMessage(Display)
        

    def changeColor(self, Display, newColor):
        pygame.draw.rect(Display, newColor, (self.x_pos,self.y_pos,self.width,self.height) )
        self.displayMessage(Display)

    def isClicked(self, isPressed):
        if isPressed[0] == 1:
            return True;
        

        
def gameIntro():
    intro = True;
	
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        displayMessageCenter("Hello, World!", black)
        girl(x,y)
        button_x = (displayWidth/2) - 100
        button_y = displayHeight*(2/3)
        playButton = button(green, button_x, button_y,200,100, "Start")
        
        mouse = pygame.mouse.get_pos()
        #change color if mouse hovers over it
        if playButton.x_pos < mouse[0] < (playButton.x_pos + playButton.width) and playButton.y_pos < mouse[1] < (playButton.y_pos + playButton.height) :
            playButton.changeColor(gameDisplay, bright_green)
            clicked = pygame.mouse.get_pressed()
            if playButton.isClicked(clicked):
                gameLoop()
        else:
            playButton.drawB(gameDisplay)

        pygame.display.update()
        clock.tick(15)

def gameLoop():
    gameDisplay.fill(black)
    pygame.display.update()
    pygame.time.wait(1500)
    
    loop = True
    
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(black)
        displayMessageCenter("Game Over", white)
        button_x = (displayWidth/2) - 100
        button_y = displayHeight*(2/3)
        restart = button(red, button_x, button_y,200,100, "Play Again")

        mouse = pygame.mouse.get_pos()
        #change color if mouse hovers over it
        if restart.x_pos < mouse[0] < (restart.x_pos + restart.width) and restart.y_pos < mouse[1] < (restart.y_pos + restart.height) :
            restart.changeColor(gameDisplay, bright_red)
            clicked = pygame.mouse.get_pressed()
            if restart.isClicked(clicked):
                gameLoop()
        else:
            restart.drawB(gameDisplay)

        pygame.display.update()
        clock.tick(15)
        
        
gameIntro()
#gameLoop()
# how we exit pygame
pygame.quit()
quit()
