'''
Created on February 11, 2019
@author: briankim
'''

import pygame
from pygame.locals import *
import sys
import time
import os
from gameConstants import *



#set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")





class Spider(pygame.sprite.Sprite):
    '''
    The Spider class sets up spider shaped sprite when passed
    a starting location and speed.

    Include methods for changing speed as well as collision detection
    '''
    
    speed = 0
    
    def __init__(self, x, speed):
        pygame.sprite.Sprite.__init__(self)

        #Change this later to spider image
        self.image = pygame.image.load(os.path.join(img_folder, "spider.png")).convert()
        self.image = pygame.transform.scale(self.image, (31,34))
        self.image.set_colorkey(Color.BLACK.value)
        self.rect = self.image.get_rect()
        self.rect.center = (x, 0)

       

        
        self.speed = speed
        self.delta = 0


    def update(self):
        if self.rect.bottom >= ((4 * Dimensions.HEIGHT.value/5)):
            self.delta = -self.speed
            
        if self.rect.top < (0):
            self.delta = self.speed

        
        self.rect.y += self.delta



            

 
            
        
       # print(self.rect.y)


        '''    if self.rect.top > Dimensions.HEIGHT.value:
                self.rect.bottom = 0

'''
    
        
