import pygame

class Player: #defining blueprint named player
    def __init__(self, name):  #constructor
        self.name=name
        self.health=5
        self.max_health=5
        self.score=0
        self.minutes=0
        self.rect=pygame.Rect(100, 500, 50, 80) #start at x100 y500 50wide 80tall
        self.speed=5
# self means each object its own score health name...
    def take_damage(self, amount): # method
        self.health=self.health-amount
        if self.health<0:
            self.health=0
        print(self.name, "was hit! Health is now", self.health)

    def heal(self, amount):
        self.health=self.health+amount
        if self.health> self.max_health:
            self.health=self.max_health
        print(self.name, "healed! health is now", self.health)

    def is_alive(self):
        return self.health>0

    def add_minutes(self,amount):
        self.minutes=self.minutes+amount
        print(self.name,"has survived for", self.minutes,"minutes")

    def update(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, (230, 190, 90), self.rect)