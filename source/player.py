import time, pygame
from gameConstants import Color, Dimensions, PlayerConst


class Player:
    def __init__(self, x=10, y=Dimensions.HEIGHT.value- PlayerConst.GROUND_DIST.value):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, PlayerConst.WIDTH.value, PlayerConst.HEIGHT.value)
        self.events = []
        self.pressed = None
        self.orientation = 'RIGHT'
        self.health = PlayerConst.HEALTH.value
        self.score = 0
        self.immune_time = 0
        self.index = 0
        self.state = 0
        self.F = 0
        self.isJump = 0
        self.v = PlayerConst.JUMP_V.value
        self.m = PlayerConst.MASS.value
        self.speed = PlayerConst.SPEED.value

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
            if self.y >= Dimensions.HEIGHT.value-PlayerConst.GROUND_DIST.value:
                self.y = Dimensions.HEIGHT.value-PlayerConst.GROUND_DIST.value
                self.isJump = 0
                self.v = 10
            self.rect = pygame.Rect(self.x, self.y, PlayerConst.WIDTH.value, PlayerConst.HEIGHT.value)

    def move(self, direction):
        if self.state == 0:
            self.state += 1
            self.index += 0.25
        else:
            self.state = 0
        if self.index >= PlayerConst.PLAYER_FRAME.value:
            self.index = 0

        if direction == 'left' and self.x >= 10:
            self.orientation = 'LEFT'
            self.x -= self.speed
        elif direction == 'right' and self.x < Dimensions.WIDTH.value:
            self.orientation = 'RIGHT'
            self.x += self.speed
        elif direction == 'jump' and self.y <= Dimensions.HEIGHT.value - PlayerConst.GROUND_DIST.value:
            self.isJump = 1

        # print (self.y, self.F)
        self.rect = pygame.Rect(self.x, self.y, PlayerConst.WIDTH.value, PlayerConst.HEIGHT.value)

    def hit(self):
        if time.time() - self.immune_time >= 3:
            self.flash = 30
            self.health -= 1
            self.immune_time = time.time()
        return self.health <= 0

    def pick(self):
        self.score += 1
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
