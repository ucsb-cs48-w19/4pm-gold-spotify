import pygame
from gameConstants import Dimensions, SpiderConst
# from gameConstants import Sounds

class Spider(pygame.sprite.Sprite):
    '''
    The Spider class sets up spider shaped sprite when passed
    a starting location and speed.
    Include methods for changing speed as well as collision detection
    '''

    def __init__(self, x, speed, y = 0):
        pygame.sprite.Sprite.__init__(self)
        # self.mixer = pygame.mixer.music.load(Sounds.SpiderSqueak.value)
      
        self.rect = pygame.Rect(x, y, SpiderConst.WIDTH.value, SpiderConst.HEIGHT.value)
        self.rect.center = (x, y)

        self.speed = speed
        self.delta = speed
        self.y = y
        self.x = x

    def update(self):
        if self.rect.bottom > ((4 * Dimensions.HEIGHT.value / 5)):
            self.delta = -self.speed

        if self.rect.top < (0):
            self.delta = self.speed

        self.rect.y += self.delta

#    def squeak(self):
#        self.mixer.play()


class Hor_Spider(pygame.sprite.Sprite):
    '''
        The Spider class sets up spider shaped sprite when passed
        a starting location and speed.
        
        Include methods for changing speed as well as collision detection
        '''
    
    speed = 0
    
    def __init__(self, speed, x_start = 0, x_end = Dimensions.WIDTH.value, y = 4* Dimensions.HEIGHT.value/5):
        pygame.sprite.Sprite.__init__(self)
    
        self.rect = pygame.Rect(x_start, y, SpiderConst.WIDTH.value, SpiderConst.HEIGHT.value)
        self.rect.center = (x_start, y)
       
        self.x_end = x_end
        self.x_start = x_start
        self.y = y
         
        self.speed = speed
        self.delta = speed
    
    
    def update(self):
        if self.rect.right >= (self.x_end):
            self.delta = -self.speed
        
        if self.rect.left < (self.x_start):
            self.delta = self.speed
        
        
        self.rect.x += self.delta

