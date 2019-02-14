import time, pygame


class Player:
    def __init__(self, x=50, y=450):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, 25, 50)
        self.events = []
        self.pressed = None
        self.health = 100
        self.score = 0
        self.immune_time = 0

    def update(self, events):
        self.events = events

    def move(self, direction):
        if direction == 'left' and self.x >= 10:
            self.x -= 10
        elif direction == 'right' and self.x < 780:
            self.x += 10
        self.rect = pygame.Rect(self.x, self.y, 25, 50)

    def hit(self):
        if time.time() - self.immune_time >= 3:
            self.health -= 20
            self.immune_time = time.time()
        return self.health <= 0

    def pick(self):
        self.score += 1
        return self.score

    def refresh(self, events):
        self.update(events)
