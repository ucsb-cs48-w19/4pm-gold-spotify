import time, pygame
from gameConstants import Color, Dimensions


class Player:
    def __init__(self, x=10, y=440):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, 66, 110)
        self.events = []
        self.pressed = None
        self.health = 5
        self.score = 0
        self.immune_time = 0
        self.index = 0
        self.state = 0
        self.F = 0
        self.isJump = 0
        self.v = 10
        self.m = 2
        self.speed = 8

        self.jump_s = pygame.mixer.Sound("../resources/sound/jump.wav")
        self.collect_s = pygame.mixer.Sound("../resources/sound/Pickup_Coin.wav")
        self.hit_s = pygame.mixer.Sound("../resources/sound/hit.wav")

    def update(self, events):
        self.events = events
        if self.isJump:

            # Calculate force (F). F = 0.5 * mass * velocity^2.

            if self.v > 0:
                self.F = (0.5 * self.m * (self.v * self.v))
            else:
                self.F = -(0.5 * self.m * (self.v * self.v))

            # Change position
            self.y = self.y - self.F / 2
            # Change velocity
            self.v = self.v - 1

            # If ground is reached, reset variables.
            if self.y >= 450:
                self.y = 450
                self.isJump = 0
                self.v = 10
            self.rect = pygame.Rect(self.x, self.y, 66, 110)

    def move(self, direction):
        if self.state == 0:
            self.state += 1
            self.index += 0.5
        else:
            self.state = 0
        if self.index >= Dimensions.PLAYER_FRAME.value:
            self.index = 0

        if direction == 'left' and self.x >= 10:
            self.x -= self.speed
        elif direction == 'right' and self.x < 780:
            self.x += self.speed
        elif direction == 'jump' and self.y <= 450:
            pygame.mixer.Sound.play(self.jump_s)
            self.isJump = 1

        # print (self.y, self.F)
        self.rect = pygame.Rect(self.x, self.y, 66, 110)

    def hit(self):
        if time.time() - self.immune_time >= 3:
            self.flash = 30
            self.health -= 1
            self.immune_time = time.time()
            pygame.mixer.Sound.play(self.hit_s)
        return self.health <= 0

    def pick(self):
        self.score += 1
        pygame.mixer.Sound.play(self.collect_s)
        return self.score

    def blink(self):
        if time.time() - self.immune_time < 3:
            if self.flash == 0:
                self.flash = 30
            self.flash -= 1
            return self.flash > 15
        return False

    def refresh(self, events):
        self.update(events)
