#helloWorld.py

import pygame

#initiate pygame and all modules that come with it
pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = ()
#next want to set up window/surface
gameDisplay = pygame.display.set_mode((display_width,display_height)) #width and height as a tuple

pygame.display.set_caption("Hello World!")

#Next want to define the game's clock (frames/sec)
clock = pygame.time.Clock()

#Every game needs a game loop, the only thing that breaks out is a crash or a quit
#pygame grabs all events for you; pygame.event.get() gets any event that happened (move mouse, click)

#pygame.QUIT is when someone click the x in a window to close it

#we want code to run for all frames?

#to update display: pygame.display.update()(can put parameters so that only
#certain things are updated; otherwise updates entire surface) OR
#pygame.display.flip() - always just updates the entire surface

#we want to define our frames per sec, how fast are we gonna do this stuff
clock.tick(60) #for parameter put the number of frames per second you want
             #if you want something to run fast but smooth then increase frames/sec


# how we exit pygame
pygame.quit()
quit()
