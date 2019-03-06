import pygame
from world import World

from gameConstants import Color
from gameConstants import Dimensions
from gameConstants import Fonts

class Display:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.clock = pygame.time.Clock()
        self.clock.tick(60)
        self.canvas = pygame.display.set_mode((Dimensions.WIDTH.value, Dimensions.HEIGHT.value), 0, 32)
        self.events = []
        self.world = World()

        self.bg = pygame.Surface([0, 0], pygame.SRCALPHA)
        self.bg = pygame.image.load("../resources/Backgrounds/Welcome.png").convert_alpha()
        self.bg_images = {}
        self.bg_images["Welcome"] = pygame.image.load("../resources/Backgrounds/Welcome.png").convert_alpha()
        self.bg_images["LevelOne"] = pygame.image.load("../resources/Backgrounds/LevelOneBackground.png").convert_alpha()
        self.bg_images["End"] = pygame.image.load("../resources/Backgrounds/winPLACEHOLDER.png")
        self.bg_images["Map"] = pygame.image.load("../resources/Backgrounds/map_screen.png").convert_alpha()
        self.bg = pygame.transform.scale(self.bg, (Dimensions.WIDTH.value, Dimensions.HEIGHT.value))
        self.rect = self.bg.get_rect()

        self.player_images = []
        self.player_images.append(pygame.image.load('../resources/PlayerFrames/minWalk1.png').convert_alpha())
        self.player_images.append(pygame.image.load('../resources/PlayerFrames/minWalk2.png').convert_alpha())
        self.player_images.append(pygame.image.load('../resources/PlayerFrames/minWalk3.png').convert_alpha())
        self.player_images.append(pygame.image.load('../resources/PlayerFrames/minWalk4.png').convert_alpha())
        self.player_images.append(pygame.image.load('../resources/PlayerFrames/minWalk5.png').convert_alpha())
        self.player_images.append(pygame.image.load('../resources/PlayerFrames/minWalk6.png').convert_alpha())

        self.food_image = [pygame.image.load("../resources/Berry/berrySmall.png").convert_alpha(),
                            pygame.image.load("../resources/Pumpkin/pumpkin.png").convert_alpha(),
                            pygame.image.load("../resources/Turkey/turkey.png").convert_alpha()]
        self.berry_image_big = pygame.image.load("../resources/Berry/berry_big.png").convert_alpha()
        self.pumpkin_image_big = pygame.image.load("../resources/Pumpkin/pumpkin_big.png").convert_alpha()
        self.turkey_image_big = pygame.image.load("../resources/Turkey/turkey_big.png").convert_alpha()
        self.turkey_image_big = pygame.transform.scale(self.turkey_image_big, (70, 70))
        self.pumpkin_image_big = pygame.transform.scale(self.pumpkin_image_big, (70, 70))
        self.berry_image_big = pygame.transform.scale(self.berry_image_big, (70, 70))


        self.spider_image = pygame.image.load("../resources/Spider/spider.png").convert_alpha()
        self.spider_image = pygame.transform.scale(self.spider_image, (35, 30))
        self.heart = pygame.image.load('../resources/Heart/heart.png').convert_alpha()
        self.heart = pygame.transform.scale(self.heart, (30, 30))
        self.heart_b = pygame.image.load('../resources/Heart/heart_b.png').convert_alpha()
        self.heart_b = pygame.transform.scale(self.heart_b, (30, 30))

        #background music playing
        self.background_s = pygame.mixer.music.load("../resources/sound/background_music.ogg")
        self.jump_s = pygame.mixer.Sound("../resources/sound/jump.wav")
        self.collect_s = pygame.mixer.Sound("../resources/sound/Pickup_Coin.wav")
        self.hit_s = pygame.mixer.Sound("../resources/sound/hit.wav")
        pygame.mixer.music.set_volume(0.4)

    def start(self):
        pygame.mixer.music.play(loops=-1)
        self.refresh()

    def draw_game(self, texts, buttons, objects, ground): #, obstacles):
        # insert image here, look at player's image code to create image and use bilt to build it
        if self.world.state == 0:
            self.bg = self.bg_images["Welcome"]
            self.bg = pygame.transform.scale(self.bg, (Dimensions.WIDTH.value, Dimensions.HEIGHT.value))

        if self.world.state == 1:
            self.bg = self.bg_images["Welcome"]
            self.bg = pygame.transform.scale(self.bg, (Dimensions.WIDTH.value, Dimensions.HEIGHT.value))

        if self.world.state in [3, 6]:
            self.bg = self.bg_images["LevelOne"]
            self.bg = pygame.transform.scale(self.bg, (Dimensions.WIDTH.value, Dimensions.HEIGHT.value))
        # map screen

        self.canvas.blit(self.bg, self.rect)

        if ground is not None:
            for s in ground.spiders:
                self.canvas.blit(self.spider_image, s.rect)
            #Draw Web
                pygame.draw.line(self.canvas, Color.WHITE.value, (s.x + 13,0), (s.x + 13, s.rect.top + 4), 2)
            for h in ground.h_spiders:
                self.canvas.blit(self.spider_image, h.rect)
            for o in ground.foods:
                self.canvas.blit(self.food_image[self.world.level - 1], o.rect)

        if self.world.pause:
            self.transparentRect = pygame.Surface((400, 600))
            self.transparentRect.set_alpha(128)
            self.transparentRect.fill((255, 255, 255))
            self.canvas.blit(self.transparentRect, (200, 0))

        # draw all the buttons
        for button in buttons:
            pygame.draw.rect(self.canvas, button[4], (button[0], button[1], button[2], button[3]))
        '''
        #draw in the obstacles
        for block in obstacles:
            pygame.draw.rect(self.canvas, Color.BLACK.value, (block[0], block[1], block[2], block[3]))
        '''
        # draw all texts
        for t in texts:
            text = t[4].render(t[0], True, t[1])
            textRect = text.get_rect()
            textRect.center = (t[2], t[3])
            self.canvas.blit(text, textRect)

        if self.world.state == 2:
            self.bg = self.bg_images["Map"]
            self.bg = pygame.transform.scale(self.bg, (Dimensions.WIDTH.value, Dimensions.HEIGHT.value))
            self.canvas.blit(self.berry_image_big, (200, 200))
            self.canvas.blit(self.pumpkin_image_big, (310, 400))
            self.canvas.blit(self.turkey_image_big, (500, 250))

        # draw all the objects
        for player in objects:
            image = self.player_images[int(player.index)]
            image = pygame.transform.scale(image, (66, 110))
            if not player.blink():
                self.canvas.blit(image, player.rect)

            if player.isJumpSound:
                pygame.mixer.Sound.play(self.jump_s)
                player.isJumpSound = 0

            if player.isHitSound:
                pygame.mixer.Sound.play(self.hit_s)
                player.isHitSound = 0

            if player.isCollectSound:
                pygame.mixer.Sound.play(self.collect_s)
                player.isCollectSound = 0

            # TODO: Hard coded max health
            for i in range(5):
                if i < player.health:
                    self.canvas.blit(self.heart, (600 + i * 40, 10))
                else:
                    self.canvas.blit(self.heart_b, (600 + i * 40, 10))
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
            #texts, buttons, objects, ground, obstacles = self.world.refresh(self.events)
            texts, buttons, objects, ground = self.world.refresh(self.events)
            # render them
            #self.draw_game(texts, buttons, objects, ground, obstacles)
            self.draw_game(texts, buttons, objects, ground)

