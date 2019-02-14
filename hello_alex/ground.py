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
            self.spiders.append(Spider(s[0], s[1]))
