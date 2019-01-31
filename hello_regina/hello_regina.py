import pygame
import time
import sys

pygame.init()

clock = pygame.time.Clock()

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

screen = pygame.display.set_mode((400,400))

b_x=200
b_y=200
b_width=100
b_height=50

font1 = pygame.font.Font('freesansbold.ttf', 12)
font2 = pygame.font.Font('freesansbold.ttf', 48)

def displayScreen():
    pygame.display.set_caption('Hello World')
    screen.fill(white)
    pygame.display.update()

def displayStartScreen():
    displayScreen()
    drawButton('Start Game')
    pygame.display.update()


def displayText(message, font, color, x, y):
    text = font.render(message, True, color)
    textrect = text.get_rect()
    textrect.center = (x,y)
    screen.blit(text, textrect)
    pygame.display.update()

def drawButton(message):
    pygame.draw.rect(screen, red, (b_x,b_y,b_width,b_height))
    pygame.display.update()
    displayText(message, font1, black, (b_x+(b_width/2)), (b_y+(b_height/2)))

def pushStartButton():
    if updateMousePosition() == 1:
        displayText('Game Over', font2, black, 150, 100)
        drawButton('Play Again')
        pygame.display.update()

def pushReStartButton():
    if updateMousePosition() == 1:
        displayStartScreen();

def updateMousePosition():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if b_x + b_width > mouse[0] > b_x and b_y+b_height > mouse [1] > b_y:
        if click[0] == 1:
            return 1

def playGame():
    started = 0
    while True:
        time_passed = clock.tick(50)
        
        for event in pygame.event.get():
           
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
            if event.type == pygame.MOUSEBUTTONDOWN:
                if started == 0:
                    pushStartButton()
                    started = 1
                else:
                    pushReStartButton()
                    started = 0



displayStartScreen()
playGame()
