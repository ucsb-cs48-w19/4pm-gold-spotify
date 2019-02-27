import pygame
from gameConstants import Color
from gameConstants import Dimensions
from gameConstants import Fonts
from gameConstants import Sounds

class Spider(pygame.sprite.Sprite):
    '''
    The Spider class sets up spider shaped sprite when passed
    a starting location and speed.
    Include methods for changing speed as well as collision detection
    '''

    speed = 0

    def __init__(self, x, speed):
        pygame.sprite.Sprite.__init__(self)
        # self.mixer = pygame.mixer.music.load(Sounds.SpiderSqueak.value)
        # Change this later to spider image
        self.rect = pygame.Rect(x, 0, 10, 10)
        self.rect.center = (x, 0)

        self.speed = speed
        self.delta = 0

    def update(self):
        if self.rect.bottom >= ((4 * Dimensions.HEIGHT.value / 5)):
            self.delta = -self.speed

        if self.rect.top < (0):
            self.delta = self.speed

        self.rect.y += self.delta

#    def squeak(self):
#        self.mixer.play()


