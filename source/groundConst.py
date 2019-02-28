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
                [ (100, 1),(150, 1),(200, 1), (250, 2), (300, 2), (350, 2), (400, 1), (450, 1), (500, 1), (550, 2), (600, 2), \
                  (650, 2), (700, 1), (750, 1), (800, 1)]
                ]
    ground1 = [[(100, h), (175, h), (300, h), (550, h), (250, h)], \
               [(50, 4), (100, 6), (150, 5), (200, 3), (250, 4), (330, 3), (410, 4), (500, 8), (565, 6), (600, 5), (635, 7), (720, 4), (760, 3)]]
    ground2 = [[(100, h), (200, h), (300, h), (400, h), (500, h)], \
               [(75, 5), (150, 4), (225, 5), (375, 3), (425, 9), (525, 7)]]
    ground3 = [[(70, h), (140, h), (210, h), (280, h), (350, h), (420, h), (490, h), (560, h)], \
               [(120, 3), (150, 6), (180, 3), (210, 6), (240, 3), (270, 6), (300, 3), (330, 6), (360, 3), (390, 6), (420, 3), (450, 6), (480, 3),\
                (510, 6), (540, 3), (570, 6), (600, 3), (630, 6), (660, 3), (690, 6), (720, 3), (750, 6), (780, 3)]]

    ground4 = [[(60, h), (190, h), (230, h), (430, h), (520, h), (540, h)], \
               [(90, 4), (160, 5), (200, 5), (270, 3), (340, 4), (430, 2)]]
    g = [ground0, ground1, ground2, ground3, ground4]
