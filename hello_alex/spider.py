'''
Created on February 11, 2019
@author: briankim
'''

import pygame
from pygame.locals import *
import sys
import time
from gameConstants import *




class Spider(pygame.sprite.Sprite):
    '''
    The Spider class sets up spider shaped sprite when passed
    a starting location and speed.

    Include methods for changing speed as well as collision detection
    '''

    
    def __init__(self):
        pygame.sprite.Sprite.__init(self)

        #Change this later to spider image
        self.image = pygame.Surface((50,50))
        self.image.fill(Color.GREEN.value) # Why is it .value

        self.rect = self.image.get_rect()
        self.rect.center =


        def update(self):
            self.rect.y += 5

            if self.rect.top > Dimensions.HEIGHT.value:
                self.rect.bottom = 0


        def col

        
