import pygame, time
from player import Player
from ground import Ground

from gameConstants import Color
from gameConstants import Dimensions
from gameConstants import Fonts


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
        self.start_time = 0
        self.pressed_key = None
        self.ground = None

    def update(self):
        self.mouse = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()

    def run(self):
        self.buttons = []
        self.texts = []
        self.objects = []
        self.ground = None
        if self.state == 0:
            self.texts.append(('Turkey Trot!', Color.BLACK.value, 400, 100, Fonts.BASICFONT.value))
            self.texts.append(('Start Game', Color.BLACK.value, 400, 375, Fonts.SMALLFONT.value))
            # make the button bright if mouse is on it
            if 350 + 100 > self.mouse[0] > 350 and 350 + 50 > self.mouse[1] > 350:
                self.buttons.append((350, 350, 100, 50, Color.BRIGHT_GREEN.value))
                # switch state if user click, start timer
                if self.click[0] == 1:
                    self.state = 2
                    self.start_time = time.time()
            else:
                self.buttons.append((350, 350, 100, 50, Color.GREEN.value))

        elif self.state == 1:
            self.texts.append(('Game Over!', Color.BLACK.value, 400, 100, Fonts.BASICFONT.value))
            self.texts.append(('Start Again', Color.WHITE.value, 400, 375, Fonts.SMALLFONT.value))
            # draw and detect start again button
            if 350 + 100 > self.mouse[0] > 350 and 350 + 50 > self.mouse[1] > 350:
                self.buttons.append((350, 350, 100, 50, Color.BRIGHT_GREEN.value))
                if self.click[0] == 1:
                    self.state = 2
                    self.start_time = time.time()
                    self.player = Player()
            else:
                self.buttons.append((350, 350, 100, 50, Color.GREEN.value))

        elif self.state == 2:
            self.objects.append(self.player)
            self.ground = Ground(0)

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

            # switch state if player at edge of screen
            if self.player.x >= 780:
                self.state = 3
                # TODO
                self.player.x = 30

        elif self.state == 3:
            # TODO: solve repetitive code
            self.objects.append(self.player)
            self.ground = Ground(1)
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

            # switch state if player at edge
            if self.player.x >= 780:
                self.state = 1
            if self.player.x <= 20:
                self.state = 2
                self.player.x = 780

        else:
            print("Unknown state", self.state)

    def refresh(self, events):
        # the function being called each game loop
        self.update()
        self.events = events
        self.run()
        self.player.refresh(self.events)
        return self.texts, self.buttons, self.objects, self.ground
