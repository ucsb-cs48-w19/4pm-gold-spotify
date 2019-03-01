import pygame
from world import World

from gameConstants import Color
from gameConstants import Dimensions
from gameConstants import Fonts
from world import World

class Display:
    def __init__(self):
        pygame.init()
#        pygame.mixer.init()
        self.clock = pygame.time.Clock()
        self.clock.tick(60)
        self.canvas = pygame.display.set_mode((Dimensions.WIDTH.value, Dimensions.HEIGHT.value), 0, 32)
        self.events = []
        self.world = World()

        self.bg = pygame.Surface([0, 0], pygame.SRCALPHA)
        self.bg = pygame.image.load("../resources/Backgrounds/welcomePLACEHOLDER.png").convert_alpha()
        self.bg_images = {}
        self.bg_images["Welcome"] = pygame.image.load("../resources/Backgrounds/welcomePLACEHOLDER.png").convert_alpha()
        self.bg_images["LevelOne"] = pygame.image.load("../resources/Backgrounds/LevelOneBackground.png").convert_alpha()
        self.bg_images["End"] = pygame.image.load("../resources/Backgrounds/winPLACEHOLDER.png")
        self.bg = pygame.transform.scale(self.bg, (Dimensions.WIDTH.value, Dimensions.HEIGHT.value))
        self.rect = self.bg.get_rect()

        self.player_images = []
        self.player_images.append(pygame.image.load('../resources/PlayerFrames/minWalk1.png').convert_alpha())
        self.player_images.append(pygame.image.load('../resources/PlayerFrames/minWalk2.png').convert_alpha())
        self.player_images.append(pygame.image.load('../resources/PlayerFrames/minWalk3.png').convert_alpha())
        self.player_images.append(pygame.image.load('../resources/PlayerFrames/minWalk4.png').convert_alpha())
        self.player_images.append(pygame.image.load('../resources/PlayerFrames/minWalk5.png').convert_alpha())
        self.player_images.append(pygame.image.load('../resources/PlayerFrames/minWalk6.png').convert_alpha())

        self.berry_image = pygame.image.load("../resources/Berry/berrySmall.png").convert_alpha()

        self.spider_image = pygame.image.load("../resources/Spider/spider.png").convert_alpha()
        self.spider_image = pygame.transform.scale(self.spider_image, (35, 30))

    def start(self):
        # for now, it just straight call the game loop
        self.world.start()
        self.refresh()

    def draw_game(self, texts, buttons, objects, ground):
        # insert image here, look at player's image code to create image and use bilt to build it
        self.canvas.blit(self.bg, self.rect)

        # draw all the buttons
        for button in buttons:
            pygame.draw.rect(self.canvas, button[4], (button[0], button[1], button[2], button[3]))
        # draw all the objects
        for player in objects:
            # pygame.draw.ellipse(self.canvas, Color.BLACK.value, (player.x, player.y, 25, 50))
            image = self.player_images[player.index]
            image = pygame.transform.scale(image, (50, 75))
            self.canvas.blit(image, player.rect)
            pygame.draw.rect(self.canvas, Color.GREEN.value, (650, 10, player.health, 10))
        # draw all texts
        for t in texts:
            text = t[4].render(t[0], True, t[1])
            textRect = text.get_rect()
            textRect.center = (t[2], t[3])
            self.canvas.blit(text, textRect)
        if ground is not None:
            for s in ground.spiders:
                self.canvas.blit(self.spider_image, s.rect)
            for b in ground.berries:
                self.canvas.blit(self.berry_image, b.rect)
        if self.world.state == 0:
            self.bg = self.bg_images["Welcome"]
            self.bg = pygame.transform.scale(self.bg, (Dimensions.WIDTH.value, Dimensions.HEIGHT.value))
       
        if self.world.state == 1:
            self.bg = self.bg_images["End"]
            self.bg = pygame.transform.scale(self.bg, (Dimensions.WIDTH.value, Dimensions.HEIGHT.value))
       
        if self.world.state in [2,6]:
            self.bg = self.bg_images["LevelOne"]
            self.bg = pygame.transform.scale(self.bg, (Dimensions.WIDTH.value, Dimensions.HEIGHT.value))
       
        pygame.display.flip()

    # the game loop
    def refresh(self):
        while True:
            self.events = pygame.event.get()
            for event in self.events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            # throw events to world and get lists of objects that need to render back
            texts, buttons, objects, ground = self.world.refresh(self.events)
            # render them
            self.draw_game(texts, buttons, objects, ground)
