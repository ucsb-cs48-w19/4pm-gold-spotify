import pygame
from gameConstants import Dimensions
from groundConst import LevelOne
from berry import Berry
from spider import Spider


class Ground:
    # ground object will be initialized with a 2 lists containing
    # info for the spiders and berries

    def __init__(self, level):
        self.spiders = []
        self.berries = []
        self.start(level)

    def start(self, level):
        for b in LevelOne.g.value[level][0]:
            self.berries.append(Berry(b[0], b[1]))
        for s in LevelOne.g.value[level][1]:
            self.spiders.append(Spider(s[0], s[1]*3))
            #self.spiders.append(Spider(s[0], s[1]))

            #scaling for computers with lower pixel density
            #dividing by 3 for now; if this is too slow for your
            #computer, comment out the line below and uncomment
            #the one above 
            #self.spiders.append(Spider(s[0], s[1]/3))

    def berry_pick(self, idx):
        del self.berries[idx]
