import pygame
from world import World

# TODO: figure out a way to deal with constants
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
        # for now, it just straight call the game loop
        self.refresh()

    def draw_game(self, texts, buttons, objects):
        self.canvas.fill(WHITE)
        # draw all the buttons
        for button in buttons:
            pygame.draw.rect(self.canvas, button[4], (button[0], button[1], button[2], button[3]))
        # draw all the objects
        for obj in objects:
            pygame.draw.ellipse(self.canvas, BLACK, (obj.x, obj.y, 25, 50))
        # draw all texts
        for t in texts:
            text = t[4].render(t[0], True, t[1])
            textRect = text.get_rect()
            textRect.center = (t[2], t[3])
            self.canvas.blit(text, textRect)
        # update game display
        pygame.display.update()

    # the game loop
    def refresh(self):
        while True:
            self.events = pygame.event.get()
            for event in self.events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            # throw events to world and get lists of objects that need to render back
            texts, buttons, objects = self.world.refresh(self.events)
            # render them
            self.draw_game(texts, buttons, objects)