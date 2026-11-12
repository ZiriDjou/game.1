import pygame
from settings import LEVEL_WIDTH, GROUND_Y


class Monster:
    def __init__(self,x):
        self.rect= pygame.Rect(x,GROUND_Y-50, 50, 50)
        self.speed=2
        self.direction=1 # 1 is right, -1 is is left
        self.health =4 
        self.points=10
        self.knockback_timer = 0
        self.knockback_direction=1
        self.pause_timer = 0



    def update(self):

        if self.knockback_timer>0:
            self.rect.x+= 8*self.knockback_direction
            self.knockback_timer-=1
            if self.knockback_timer==0:
                self.pause_timer=120
            return

        if self.pause_timer>0:
            self.pause_timer-=1
            return
        
        self.rect.x += self.speed*self.direction
        if self.rect.left<0 or self.rect.right>LEVEL_WIDTH:
            self.direction= -self.direction

        

    def is_alive(self):
        return self.health>0
    
    def knockback(self,direction):
        self.knockback_timer=10
        self.knockback_direction=direction

    def draw(self,screen,camera):
        pygame.draw.rect(screen, (180, 40, 60), camera.apply(self.rect))