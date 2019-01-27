import pygame, time, sys


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 200, 0)
BRIGHT_GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WIDTH = 800
HEIGHT = 600


class Display:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.clock.tick(30)
        self.canvas = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
        self.basicFont = pygame.font.SysFont(None, 50)
        self.mouse = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()
        self.start_time = 0
        # start = 0, in game = 1, end game = 2
        self.state = 0

    def start(self):
        self.refresh()

    def update(self):
        self.mouse = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()

    def draw_game(self):
        if self.state == 0:
            pygame.display.set_caption('Hello world')
            text = self.basicFont.render('Hello world!', True, WHITE, BLUE)
            textRect = text.get_rect()
            textRect.center = (self.canvas.get_rect().centerx, 100)
            self.canvas.fill(WHITE)
            self.canvas.blit(text, textRect)
            if 350 + 100 > self.mouse[0] > 350 and 350 + 50 > self.mouse[1] > 350:
                pygame.draw.rect(self.canvas, BRIGHT_GREEN, (350, 350, 100, 50))
                if self.click[0] == 1:
                    self.state = 1
                    self.start_time = time.time()
            else:
                pygame.draw.rect(self.canvas, GREEN, (350, 350, 100, 50))
            smallText = pygame.font.SysFont(None, 25)
            start_text = smallText.render('Start Game', True, WHITE)
            start_text_Rect = start_text.get_rect().center = (400, 375)
            start_text_Rect.center = (400, 375)
            self.canvas.blit(start_text, start_text_Rect)

        elif self.state == 1:
            self.canvas.fill(WHITE)
            text = self.basicFont.render('In Game', True, WHITE, BLUE)
            textRect = text.get_rect()
            textRect.center = (self.canvas.get_rect().centerx, 100)
            if time.time() - self.start_time >= 5:
                self.state = 2

        elif self.state == 2:
            text = self.basicFont.render('Game Over!', True, BLACK)
            textRect = text.get_rect()
            textRect.center = (self.canvas.get_rect().centerx, 100)
            self.canvas.fill(WHITE)
            self.canvas.blit(text, textRect)
            if 350 + 100 > self.mouse[0] > 350 and 350 + 50 > self.mouse[1] > 350:
                pygame.draw.rect(self.canvas, BRIGHT_GREEN, (350, 350, 100, 50))
                if self.click[0] == 1:
                    self.state = 1
                    self.start_time = time.time()
            else:
                pygame.draw.rect(self.canvas, GREEN, (350, 350, 100, 50))
            smallText = pygame.font.SysFont(None, 25)
            start_text = smallText.render('Start Again', True, WHITE)
            start_text_Rect = start_text.get_rect()
            start_text_Rect.center = (400, 375)
            self.canvas.blit(start_text, start_text_Rect)

        else:
            print("Unknown state", self.state)
        pygame.display.update()

    def refresh(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            self.update()
            self.draw_game()


if __name__ == "__main__":
    d = Display()
    d.start()
