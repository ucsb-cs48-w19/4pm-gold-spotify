class Player:
    def __init__(self, x=50, y=450):
        self.x = x
        self.y = y
        self.events = []
        self.pressed = None

    def update(self, events):
        self.events = events

    def move(self, direction):
        if direction == 'left' and self.x >= 10:
            self.x -= 10
        elif direction == 'right' and self.x < 780:
            self.x += 10

    def refresh(self, events):
        self.update(events)
