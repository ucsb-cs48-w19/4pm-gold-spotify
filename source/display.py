import pygame
from world import World

from gameConstants import Color, Dimensions, Fonts, PlayerConst, BerryConst, SpiderConst

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
        self.bg = pygame.image.load("../resources/Backgrounds/Welcome.png").convert_alpha()
        self.bg_images = {}
        self.bg_images["Welcome"] = pygame.image.load("../resources/Backgrounds/Welcome.png").convert_alpha()
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
        self.spider_image = pygame.transform.scale(self.spider_image, (SpiderConst.WIDTH.value, SpiderConst.HEIGHT.value))
        self.heart = pygame.image.load('../resources/Heart/heart.png').convert_alpha()
        self.heart = pygame.transform.scale(self.heart, (PlayerConst.HEART_DIM.value, PlayerConst.HEART_DIM.value))
        self.heart_b = pygame.image.load('../resources/Heart/heart_b.png').convert_alpha()
        self.heart_b = pygame.transform.scale(self.heart_b, (PlayerConst.HEART_DIM.value, PlayerConst.HEART_DIM.value))

    def start(self):
        # for now, it just straight call the game loop
        self.world.start()
        self.refresh()

    def draw_game(self, texts, buttons, objects, ground): #, obstacles):
        # insert image here, look at player's image code to create image and use bilt to build it
        self.canvas.blit(self.bg, self.rect)
        
        
        # draw all the buttons
        for button in buttons:
            # weirdly specific case here- just wanted translucent title screen button
            if button[4] == Color.WHITE.value and self.world.state == 0:
                self.transparentRect = pygame.Surface((button[2],button[3]))
                self.transparentRect.set_alpha(128)
                self.transparentRect.fill((255,255,255))
                self.canvas.blit(self.transparentRect,(button[0],button[1]))
            else:
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
        if ground is not None:
            for s in ground.spiders:
                self.canvas.blit(self.spider_image, s.rect)
            #Draw Web
                pygame.draw.line(self.canvas, Color.WHITE.value, (s.x + 13,0), (s.x + 13, s.rect.top + 4), 2)
            for h in ground.h_spiders:
                self.canvas.blit(self.spider_image, h.rect)
            for b in ground.berries:
                self.canvas.blit(self.berry_image, b.rect)
        if self.world.state == 0:
            self.bg = self.bg_images["Welcome"]
            self.bg = pygame.transform.scale(self.bg, (Dimensions.WIDTH.value, Dimensions.HEIGHT.value))
       
        if self.world.state == 1:
            self.bg = self.bg_images["End"]
            self.bg = pygame.transform.scale(self.bg, (Dimensions.WIDTH.value, Dimensions.HEIGHT.value))
            self.canvas.fill(Color.BLACK.value)
        if self.world.state in [2,6]:
            self.bg = self.bg_images["LevelOne"]
            self.bg = pygame.transform.scale(self.bg, (Dimensions.WIDTH.value, Dimensions.HEIGHT.value))
      
 # draw all the objects
        for player in objects:
            image = self.player_images[int(player.index)]
            image = pygame.transform.scale(image, (PlayerConst.WIDTH.value, PlayerConst.HEIGHT.value))
            if not player.blink():
                if player.orientation== 'RIGHT':
                    self.canvas.blit(image, player.rect)
                else:
                    self.canvas.blit(pygame.transform.flip(image,True, False), player.rect)
            # TODO: Hard coded max health
            self.transparentRect = pygame.Surface((Dimensions.WIDTH.value-50,PlayerConst.HEART_DIM.value))
            self.transparentRect.set_alpha(200)
            self.transparentRect.fill((255,255,255))
            self.canvas.blit(self.transparentRect,(Dimensions.WIDTH.value-300,10))

            for i in range(5):
                if i < player.health:
                    self.canvas.blit(self.heart, ((Dimensions.WIDTH.value-250)+ i * 40, 10))
                else:
                    self.canvas.blit(self.heart_b, ((Dimensions.WIDTH.value-250) + i * 40, 10))
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
