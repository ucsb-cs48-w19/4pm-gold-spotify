import pygame
import random
from gameConstants import *
from spider import *

pygame.init() #initialez pygame
pygame.mixer.init() #initalizes  mixer (handles sounds)

#put FPS into constants
FPS = 30 

#create window
screen = pygame.display.set_mode((Dimensions.WIDTH.value, Dimensions.HEIGHT.value))
pygame.display.set_caption("Spider Test")
clock = pygame.time.Clock()

spider1 = Spider(100,10)
spider2 = Spider(200,20)
spider3 = Spider(300,10)
spider4 = Spider(450,20)
spider5 = Spider(650,35)


all_Spiders = pygame.sprite.Group()

all_Spiders.add(spider1)
all_Spiders.add(spider2)
all_Spiders.add(spider3)
all_Spiders.add(spider4)
all_Spiders.add(spider5)






#Game Loop
running = True
while running:
    clock.tick(FPS)

    
    #Process input (events)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Update
    all_Spiders.update()



    #Draw / Render
    screen.fill(Color.WHITE.value) #Draw
    all_Spiders.draw(screen)
    '''Double Buffering:
        1. Drawing (back side)
        2. Display (front side) '''
    pygame.display.flip() # Display
    



#Quit after loop
pygame.quit()
