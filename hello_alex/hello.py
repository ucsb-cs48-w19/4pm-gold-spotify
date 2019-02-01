import pygame, time, sys


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


class Display:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.clock.tick(30)
        self.canvas = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
        self.events = []
        self.world = World()

    def start(self):
        self.refresh()

    def draw_game(self, texts, buttons, objects):
        self.canvas.fill(WHITE)
        for button in buttons:
            pygame.draw.rect(self.canvas, button[4], (button[0], button[1], button[2], button[3]))
        for obj in objects:
            pygame.draw.ellipse(self.canvas, BLACK, (obj.x, obj.y, 25, 50))
        for t in texts:
            text = t[4].render(t[0], True, t[1])
            textRect = text.get_rect()
            textRect.center = (t[2], t[3])
            self.canvas.blit(text, textRect)
        pygame.display.update()

    def refresh(self):
        while True:
            self.events = pygame.event.get()
            for event in self.events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            texts, buttons, objects = self.world.refresh(self.events)
            self.draw_game(texts, buttons, objects)


class World:
    def __init__(self):
        self.player = Player()
        self.events = []
        self.buttons = []
        self.texts = []
        self.objects = []
        self.mouse = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()
        # start = 0, in game = 1, end game = 2
        self.state = 0
        self.start_time = 0

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
            if 350 + 100 > self.mouse[0] > 350 and 350 + 50 > self.mouse[1] > 350:
                self.buttons.append((350, 350, 100, 50, BRIGHT_GREEN))
                if self.click[0] == 1:
                    self.state = 1
                    self.start_time = time.time()
            else:
                self.buttons.append((350, 350, 100, 50, GREEN))

        elif self.state == 1:
            # TODO: LINE
            # pygame.draw.line(self.canvas, BLACK, (0, 500), (800, 500))
            self.objects.append(self.player)
            if time.time() - self.start_time >= 10:
                self.state = 2

        elif self.state == 2:
            self.texts.append(('Game Over!', BLACK, 400, 100, BASICFONT))
            self.texts.append(('Start Again', WHITE, 400, 375, SMALLFONT))
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
        self.update()
        self.events = events
        self.run()
        self.player.refresh(self.events)
        return self.texts, self.buttons, self.objects


class Player:
    def __init__(self, x=50, y=450):
        self.x = x
        self.y = y
        self.events = []
        self.pressed = None

    def update(self, events):
        self.events = events

    def refresh(self, events):
        self.update(events)
        if self.pressed is not None:
            if self.pressed == pygame.K_a and self.x >= 10:
                self.x -= 10
            elif self.pressed == pygame.K_d and self.x < 780:
                self.x += 10
        for event in self.events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and self.x >= 10:
                    self.x -= 10
                    self.pressed = pygame.K_a
                elif event.key == pygame.K_d and self.x < 780:
                    self.x += 10
                    self.pressed = pygame.K_d
                else:
                    print("Unknown key")
            elif event.type == pygame.KEYUP and self.pressed is not None and event.key == self.pressed:
                self.pressed = None


if __name__ == "__main__":
    d = Display()
    d.start()
