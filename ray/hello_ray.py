

import pygame
import time


pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
grey = (128, 128, 128)
red = (200, 0, 0)
green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
blue = (0, 0, 255)

display_width = 800
display_height = 600

smallText = pygame.font.SysFont('comicsansms', 20)
largeText = pygame.font.SysFont('comicsansms', 115)

gameDisplay = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()



#   Img = pygame.image.load('cloud.jpeg')


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
    pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(textSurf, textRect)

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        if click[0] == 1 and action!=None:
            action()




def quitgame():
    pygame.quit()
    quit()


def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        TextSurf, TextRect = text_objects('Turkey-Trot!', largeText)
        TextRect.center = ((display_width/2), (display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        button("Start", 150, 450, 100, 50, green, bright_green, game_loop)
        button("Quit", 550, 450, 100, 50, red, bright_red, quitgame)
        pygame.display.update()
        clock.tick(60)


def game_loop():
    gameloop = True
    while gameloop:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        TextSurf, TextRect = text_objects('Blank Page', largeText)
        #set center
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)

        button("Again?", 150, 450, 100, 50, blue, bright_green, game_intro)
        button("Quit?", 550, 450, 100, 50, red, bright_red, quitgame)
        pygame.display.update()
        clock.tick(60)


pygame.display.update()
clock.tick(60)


game_intro()
pygame.quit()
quit()

