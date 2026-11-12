import pygame
from settings import LEVEL_WIDTH, GROUND_Y



class Player: #defining blueprint named player
    def __init__(self, name):  #constructor
        self.name=name
        self.health=5
        self.max_health=5
        self.score=0
        self.minutes=0
        self.rect=pygame.Rect(100, 500, 50, 80) #start at x100 y500 50wide 80tall
        self.speed=5
        self.velocity_y=0
        self.gravity=1
        self.jump_strength=-18
        self.on_ground=False
        self.ground_y= GROUND_Y
        self.facing = 1
        self.invincible_timer = 0
        self.knockback_timer = 0
        self.knockback_direction = 1
# self means each object its own score health name...
    def take_damage(self, amount): # method to take damage also has the thing to unable overflowing the limits or whatever (encapsulation shit thingy)
        self.health=self.health-amount
        if self.health<0:
            self.health=0
        print(self.name, "was hit! Health is now", self.health)

    def get_hurt(self, amount, direction):
        if not self.is_alive():
            return
        if self.invincible_timer > 0:
            return
        self.take_damage(amount)
        self.invincible_timer = 60
        self.knockback_timer = 10
        self.knockback_direction = direction

    def attack(self):
        if self.facing ==1:
            return pygame.Rect(self.rect.right, self.rect.y, 40, self.rect.height)
        return pygame.Rect(self.rect.left-40, self.rect.y, 40, self.rect.height)

    def heal(self, amount): # methos to heal player same as take damage method
        self.health=self.health+amount
        if self.health> self.max_health:
            self.health=self.max_health
        print(self.name, "healed! health is now", self.health)

    def is_alive(self): # method that checks if player dead returning true or false
        return self.health>0

    def add_minutes(self,amount): # method that counts minutes stressing da player
        self.minutes=self.minutes+amount
        print(self.name,"has survived for", self.minutes,"minutes")

    def update(self):   # method that moves player left right i think 

        if self.invincible_timer > 0:
            self.invincible_timer -= 1

        if self.knockback_timer > 0:
            self.rect.x += 8 * self.knockback_direction
            self.knockback_timer -= 1

        if self.knockback_timer == 0:
            keys=pygame.key.get_pressed()
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                self.rect.x -= self.speed
                self.facing=-1

            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                self.rect.x += self.speed
                self.facing=1

            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.right> LEVEL_WIDTH:
                self.rect.right = LEVEL_WIDTH


            if(keys[pygame.K_SPACE] or keys[pygame.K_UP] or keys[pygame.K_w]) and self.on_ground:
                self.velocity_y=self.jump_strength

            self.velocity_y += self.gravity
            self.rect.y += self.velocity_y

            if self.rect.bottom >=self.ground_y:
                self.rect.bottom=self.ground_y
                self.velocity_y=0
                self.on_ground=True
            else:
                self.on_ground=False

    def draw(self, screen, camera): #idk wtf this method does but i believe it draws the player on the screen 
        pygame.draw.rect(screen, (230, 190, 90), camera.apply(self.rect)) # draw on screen/the color/the size and coordinates to draw