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
            self.texts.append(('Turkey Trot!', Color.BLACK.value, 400, 100, Fonts.BASICFONT.value))
            self.texts.append(('Start Game', Color.BLACK.value, 400, 375, Fonts.SMALLFONT.value))
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
            self.texts.append(('Game Over!', Color.BLACK.value, 400, 100, Fonts.BASICFONT.value))
            self.texts.append(('Start Again', Color.WHITE.value, 400, 375, Fonts.SMALLFONT.value))
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

        # ground 1
        elif self.state == 2:
            self.objects.append(self.player)

            self.user_input()
            for s in self.ground[self.state - 2].spiders:
                if self.check_col(self.player, s):
                    if self.player.hit():
                        self.state = 1
            for b_idx, b in enumerate(self.ground[self.state - 2].berries):
                if self.check_col(self.player, b):
                    self.player.pick()
                    self.ground[self.state - 2].berry_pick(b_idx)
            # switch state if player at edge of screen
            if self.player.x >= 780:
                self.state += 1
                self.player.x = 30
            self.texts.append(
                ('Your Score:' + str(self.player.score), Color.BLACK.value, 50, 25, Fonts.SMALLFONT.value))

        # ground 2, 3, 4
        elif self.state in [3, 4, 5]:
            self.objects.append(self.player)

            self.user_input()
            for s in self.ground[self.state - 2].spiders:
                if self.check_col(self.player, s):
                    if self.player.hit():
                        self.state = 1
            for b_idx, b in enumerate(self.ground[self.state - 2].berries):
                if self.check_col(self.player, b):
                    self.player.pick()
                    self.ground[self.state - 2].berry_pick(b_idx)
            # switch state if player at edge
            if self.player.x >= 780:
                self.state += 1
                self.player.x = 30
            if self.player.x <= 20:
                self.state -= 1
                self.player.x = 780
            self.texts.append(
                ('Your Score:' + str(self.player.score), Color.BLACK.value, 50, 25, Fonts.SMALLFONT.value))

        # ground 5
        elif self.state == 6:
            self.objects.append(self.player)

            self.user_input()
            for s in self.ground[self.state - 2].spiders:
                if self.check_col(self.player, s):
                    if self.player.hit():
                        self.state = 1
            for b_idx, b in enumerate(self.ground[self.state - 2].berries):
                if self.check_col(self.player, b):
                    self.player.pick()
                    self.ground[self.state - 2].berry_pick(b_idx)
            # switch state if player at edge
            if self.player.x >= 780:
                self.state = 1
            if self.player.x <= 20:
                self.state -= 1
                self.player.x = 780
            self.texts.append(
                ('Your Score:' + str(self.player.score), Color.BLACK.value, 50, 25, Fonts.SMALLFONT.value))

        else:
            print("Unknown state", self.state)

    def check_col(self, sprite1, sprite2):
        return pygame.sprite.collide_rect(sprite1, sprite2)

    def user_input(self):
        # detect user key press, tell player to move, record key pressed until key up
        if self.pressed_key is not None:
            if self.pressed_key == pygame.K_a:
                self.player.move('left')
            elif self.pressed_key == pygame.K_d:
                self.player.move('right')
        for event in self.events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.player.move('left')
                    self.pressed_key = pygame.K_a
                elif event.key == pygame.K_d:
                    self.player.move('right')
                    self.pressed_key = pygame.K_d
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
            return self.texts, self.buttons, self.objects, self.ground[self.state - 2]
        else:
            return self.texts, self.buttons, self.objects, None
