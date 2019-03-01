# groundData.py
from enum import Enum
import pygame
from gameConstants import Dimensions

pygame.init()
pygame.font.init()

# levelOne object will hold info about the spiders/berries in each ground block. Each index in levelOne
# corresponds to a ground object

h = (4 / 5) * Dimensions.HEIGHT.value

    #g = [
    #    [[(200, h), (350, h), (500, h)], [(150, 3), (40, 4), (350, 2), (550, 5)]],
    #    [[(100, h), (175, h), (300, h), (550, h), (250, h)], [(50, 4), (100, 6), (150, 5), (200, 3), (250, 4)]],
    #    [[(100, h), (200, h), (300, h), (400, h), (500, h)],
    #     [(75, 5), (150, 4), (225, 5), (375, 3), (425, 9), (525, 7)]],
    #    [[(70, h), (140, h), (210, h), (280, h), (350, h), (420, h), (490, h), (560, h)],
    #     [(240, 3), (280, 7), (300, 5), (350, 8), (380, 4)]],
    #    [[(60, h), (190, h), (230, h), (430, h), (520, h), (540, h)],
    #     [(90, 4), (160, 5), (200, 5), (270, 3), (340, 4), (430, 2)]]
    #]

    #syntax: groundNum = [ [List of berries], [List of vertical Spiders], [List of horizontal Spiders]] -> parameters for Berry and Spider constructors
    # [List of berries] = [ (berry0_x_pos, berry0_y_pos),(berry1_x_pos, berry1_y_pos), ...]
    # [List of vertical spiders] = [ (spider0_x_pos, spider0_speed, spider0_y_pos),(spider1_x_pos, spider1_speed, spider1_y_pos), ...]
    # [List of horizontal spiders] = [ (spider0_x_start, spider0_x_end), (spider1_x_start, spider1_x_end), ...]


class LevelOne(Enum):
    y0 = 0
    y1 = Dimensions.HEIGHT.value * (1/2)
    ground0 = [ [(200, h), (350, h), (500, h)], \
                [ (100, 1, y0),(150, 1, y0),(200, 1, y0), (250, 2, y1), (300, 2, y1), (350, 2, y1), (400, 1, y0), (450, 1, y0), (500, 1, y0),\
                  (550, 2, y1), (600, 2, y1),(650, 2, y1), (700, 1, y0), (750, 1, y0), (800, 1, y0)], []]
    s1 = 1
    ground1 = [[(100, h), (175, h), (300, h), (550, h), (250, h)], \
               [(100, s1, 0),(125, s1, 40),(150, s1, 80), (175, s1, 120),(200, s1, 160), (225, s1, 200),(250, s1, 240), (275, s1, 280), (300, s1, 320),\
                (325, s1, 360), (350, s1, 400), (375, s1, 440), (400, s1, 480), (425, s1, 440), (450, s1, 400), (475, s1, 360), (500, s1, 320),\
                (525, s1, 280), (550, s1, 240), (575, s1, 200), (600, s1, 160), (625, s1, 120), (650, s1, 80), (675, s1, 40), (700, s1, 0)], []]
    ground2 = [[(100, h, ), (200, h), (300, h), (400, h), (500, h)], \
               [(75, 2, y0), (150, 2, y0), (225, 2, y0), (375, 2, y0), (425, 2, y0), (525, 2, y0)], []]
    ground3 = [[(70, h), (140, h), (210, h), (280, h), (350, h), (420, h), (490, h), (560, h)], \
               [(120, 1, y0), (180, 2, y0), (240, 1, y0), (300, 2, y0), (360, 1, y0), (420, 2, y0), (480, 1, y0), (540, 2, y0), (600, 1, y0), \
                (660, 2, y0), (720, 1, y0), (780, 2, y0)], [] ]

    ground4 = [[(60, h), (190, h), (230, h), (430, h), (520, h), (540, h)], \
               [(90, 1, y0), (500, 2, y0), (200, 1, y0), (270, 3, y0), (340, 2, y0), (430, 1, y0)], [] ]
    g = [ground0, ground1, ground2, ground3, ground4]
