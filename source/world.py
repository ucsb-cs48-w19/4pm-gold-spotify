import pygame
from player import Player
from ground import Ground

from gameConstants import Color
from gameConstants import Dimensions
from gameConstants import Fonts
from groundConst import LevelOne


class World:
    def __init__(self):
        self.player = Player()
        self.obstacles = []
        self.events = []
        self.buttons = []
        self.texts = []
        self.objects = []
        self.mouse = None
        self.click = None
        # start = 0, end game = 1, ground1 = 2, ground2 = 3
        self.state = 0
        self.pressed_key = None
        self.ground = []
        self.end = False
    def update(self):
        self.mouse = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()

    def start(self):
        # TODO: change hard code levelone
        for i in range(len(LevelOne.g.value)):
            self.ground.append(Ground(i))

    # print(self.ground)

    def run(self):
        self.buttons = []
        self.texts = []
        self.objects = []

        # start game
        if self.state == 0:
            self.buttons.append((285, 75, 230, 50, Color.WHITE.value))
            self.texts.append(('Turkey Trot!', Color.BLACK.value, 400, 100, Fonts.BASICFONT.value))
            self.texts.append(('Start Game', Color.WHITE.value, 400, 375, Fonts.SMALLFONT.value))
            # make the button bright if mouse is on it
            if 350 + 100 > self.mouse[0] > 350 and 350 + 50 > self.mouse[1] > 350:
                self.buttons.append((350, 350, 100, 50, Color.BRIGHT_GREEN.value))
                # switch state if user click
                if self.click[0] == 1:
                    self.state = 2
            else:
                self.buttons.append((350, 350, 100, 50, Color.GREEN.value))

        # end game
        elif self.state == 1:
            self.buttons.append((285, 75, 230, 50, Color.WHITE.value))
            if self.end == False:
                self.texts.append(('You didn\'t make it...', Color.BLACK.value, 400, 100, Fonts.BASICFONT.value))
            elif self.player.score >= 20 and self.end == True:
                self.texts.append(('You did it!', Color.BLACK.value, 400, 100, Fonts.BASICFONT.value))
            elif self.player.score <=20 and self.end == True:
                self.texts.append(('Not enough ingredients...', Color.BLACK.value, 400, 100, Fonts.BASICFONT.value))
            self.buttons.append((275, 175, 250, 50, Color.WHITE.value))
            self.texts.append(
            ('Your Score:' + str(self.player.score), Color.BLACK.value, 400, 200, Fonts.BASICFONT.value))
            self.texts.append(('Start Again', Color.WHITE.value, 400, 375, Fonts.SMALLFONT.value))
            self.texts.append(('Exit Game', Color.WHITE.value, 400, 525, Fonts.SMALLFONT.value))
            # draw and detect start again button
            if 350 + 100 > self.mouse[0] > 350 and 350 + 50 > self.mouse[1] > 350:
                self.buttons.append((350, 350, 100, 50, Color.BRIGHT_GREEN.value))
                if self.click[0] == 1:
                    self.state = 2
                    self.player = Player()
                    self.ground = []
                    self.start()
                    self.pressed_key = None
            else:
                self.buttons.append((350, 350, 100, 50, Color.GREEN.value))
            if 350 + 100 > self.mouse[0] > 350 and 500 + 50 > self.mouse[1] > 500:
                self.buttons.append((350, 500, 100, 50, Color.BRIGHT_RED.value))
                if self.click[0] == 1:
                    pygame.quit()
                    quit()
            else:
                self.buttons.append((350, 500, 100, 50, Color.RED.value))
        # ground 1, 2, 3, 4, 5, 6
        elif self.state == 2:
            self.trackObjects()
            self.obstacles.append((350,500,100,50))
            if self.player.x >= 780:
                self.state += 1
                self.player.x = 10
        elif self.state in [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
            self.trackObjects()
            if self.player.x >= 780:
                self.state += 1
                self.player.x = 10
            if self.player.x < 10:
                self.state -= 1
                self.player.x = 779
        elif self.state == 13:
            self.trackObjects()
            if self.player.x >= 780:
                self.end = True
                self.state = 1
            if self.player.x < 10:
                self.state -= 1
                self.player.x = 779

        else:
            print("Unknown state", self.state)

    def trackObjects(self):
        self.objects.append(self.player)
        self.user_input()
        for s in self.ground[self.state - 2].spiders:
            if self.check_col(self.player, s):
                self.player.x-=3
                if self.player.hit():
                    #s.squeak()
                    self.state = 1
        for h in self.ground[self.state - 2].h_spiders:
            if self.check_col(self.player, h):
                h.delta = -h.delta
                if self.player.hit():
                    #s.squeak()
                    self.state = 1

        for b_idx, b in enumerate(self.ground[self.state - 2].food):

            if self.check_col(self.player, b):
                self.player.pick()
                self.ground[self.state - 2].berry_pick(b_idx)
        '''
        for block in self.ground[self.state-2].obstacles:
            if block.collidepoint(self.player.x+25):
                player.x -=1
            if block.collidepoint(self.player.x):
                player.x +=1
            if block.collidepoint(self.player.y+50):
                player.y -=1
        '''   
        self.buttons.append((1, 10, 100, 30, Color.WHITE.value))
        self.texts.append(
                ('Score:' + str(self.player.score), Color.BLACK.value, 50, 25, Fonts.SMALLFONT.value))

    def check_col(self, sprite1, sprite2):
        return pygame.sprite.collide_rect(sprite1, sprite2)

    def user_input(self):
        # detect user key press, tell player to move, record key pressed until key up
        if self.pressed_key is not None:
            if self.pressed_key == pygame.K_a:
                self.player.move('left')
            elif self.pressed_key == pygame.K_d:
                self.player.move('right')
            elif self.pressed_key == pygame.K_w:
                self.player.move('jump')
        for event in self.events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.player.move('left')
                    self.pressed_key = pygame.K_a
                elif event.key == pygame.K_d:
                    self.player.move('right')
                    self.pressed_key = pygame.K_d
                elif event.key == pygame.K_w:
                    self.player.move('jump')
                else:
                    print("Unknown key")
            elif event.type == pygame.KEYUP and self.pressed_key is not None and event.key == self.pressed_key:
                self.pressed_key = None

    def refresh(self, events):
        # the function being called each game loop
        self.update()
        self.events = events
        self.run()
        self.player.refresh(self.events)
        if self.state > 1:
            for s in self.ground[self.state - 2].spiders:
                s.update()
            for h in self.ground[self.state - 2].h_spiders:
                h.update()
            return self.texts, self.buttons, self.objects, self.ground[self.state - 2]
        else:
            return self.texts, self.buttons, self.objects, None

