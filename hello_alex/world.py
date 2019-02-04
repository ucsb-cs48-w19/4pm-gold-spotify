import pygame, time
from player import Player

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 200, 0)
BRIGHT_GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WIDTH = 800
HEIGHT = 600
pygame.font.init()
BASICFONT = pygame.font.SysFont(None, 50)
SMALLFONT = pygame.font.SysFont(None, 25)


class World:
    def __init__(self):
        self.player = Player()
        self.events = []
        self.buttons = []
        self.texts = []
        self.objects = []
        self.mouse = None
        self.click = None
        # start = 0, in game = 1, end game = 2
        self.state = 0
        self.start_time = 0
        self.pressed_key = None

    def update(self):
        self.mouse = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()

    def run(self):
        self.buttons = []
        self.texts = []
        self.objects = []
        if self.state == 0:
            self.texts.append(('Hello world!', BLACK, 400, 100, BASICFONT))
            self.texts.append(('Start Game', BLACK, 400, 375, SMALLFONT))
            # make the button bright if mouse is on it
            if 350 + 100 > self.mouse[0] > 350 and 350 + 50 > self.mouse[1] > 350:
                self.buttons.append((350, 350, 100, 50, BRIGHT_GREEN))
                # switch state if user click, start timer
                if self.click[0] == 1:
                    self.state = 1
                    self.start_time = time.time()
            else:
                self.buttons.append((350, 350, 100, 50, GREEN))

        elif self.state == 1:
            # TODO: LINE
            # pygame.draw.line(self.canvas, BLACK, (0, 500), (800, 500))

            self.objects.append(self.player)

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

            # switch state if 10 sec passed from start
            if time.time() - self.start_time >= 10:
                self.state = 2

        elif self.state == 2:
            self.texts.append(('Game Over!', BLACK, 400, 100, BASICFONT))
            self.texts.append(('Start Again', WHITE, 400, 375, SMALLFONT))
            # draw and detect start again button
            if 350 + 100 > self.mouse[0] > 350 and 350 + 50 > self.mouse[1] > 350:
                self.buttons.append((350, 350, 100, 50, BRIGHT_GREEN))
                if self.click[0] == 1:
                    self.state = 1
                    self.start_time = time.time()
                    self.player = Player()
            else:
                self.buttons.append((350, 350, 100, 50, GREEN))
        else:
            print("Unknown state", self.state)

    def refresh(self, events):
        # the function being called each game loop
        self.update()
        self.events = events
        self.run()
        self.player.refresh(self.events)
        return self.texts, self.buttons, self.objects
