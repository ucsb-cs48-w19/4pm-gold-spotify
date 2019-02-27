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

    #syntax: groundNum = [ [List of berries], [List of Spiders] ] -> parameters for Berry and Spider constructors
    # [List of berries] = [ (berry0_x_pos, berry0_y_pos),(berry1_x_pos, berry1_y_pos), ...]
    # [List of spiders] = [ (spider0_x_pos, spider0_speed),(spider1_x_pos, spider1_speed), ...]



class LevelOne(Enum):
    ground0 = [ [(200, h), (350, h), (500, h)], \
                [ (200, 10), (220, 10), (240, 10), (260, 10), (280, 10), (300, 10), (320, 10), (340, 10), (360, 10), \
                  (380, 10), (400, 10), (420, 10), (440, 10), (460, 10), (480, 10), (500, 10)]
                ]
    ground1 = [[(100, h), (175, h), (300, h), (550, h), (250, h)], [(50, 4), (100, 6), (150, 5), (200, 3), (250, 4)]]
    ground2 = [[(100, h), (200, h), (300, h), (400, h), (500, h)], [(75, 5), (150, 4), (225, 5), (375, 3), (425, 9), (525, 7)]]
    ground3 = [[(70, h), (140, h), (210, h), (280, h), (350, h), (420, h), (490, h), (560, h)], \
               [(240, 3), (280, 7), (300, 5), (350, 8), (380, 4)]]
    ground4 = [[(60, h), (190, h), (230, h), (430, h), (520, h), (540, h)], [(90, 4), (160, 5), (200, 5), (270, 3), (340, 4), (430, 2)]]
    g = [ground0, ground1, ground2, ground3, ground4]
