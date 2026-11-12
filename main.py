from player import Player
from camera import Camera
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, GROUND_Y, LEVEL_WIDTH
from monster import Monster



hero = Player("Ava")

import pygame
pygame.init()
screen =pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # making the window screen and its size

pygame.display.set_caption("THE DAY THAT NEVER ENDED") #name of the game
clock = pygame.time.Clock() #honestly wallah idk

camera = Camera()
markers = [pygame.Rect(x, 540, 40, 80) for x in range(400, LEVEL_WIDTH, 400)]
monster=Monster(1000)

running=True #initialize to true so it starts
while running: # main loop
    for event in pygame.event.get():
        if event.type==pygame.QUIT: # the X button top right
            running=False

        #the attack monster loop j button
        if event.type==pygame.KEYDOWN and event.key ==pygame.K_j:
            attack_box = hero.attack()
            if monster.is_alive() and attack_box.colliderect(monster.rect):
                monster.health -=1
                print("Hit! Monster health:", monster.health)
                monster.knockback(hero.facing)
                if not monster.is_alive():
                    hero.score+=monster.points
                    print("monster defeated! Score:", hero.score)   
    hero.update()

    if monster.is_alive():
        monster.update()
        if monster.is_alive() and hero.rect.colliderect(monster.rect):
            if hero.rect.centerx < monster.rect.centerx:
                push = -1
            else:
                push = 1
            hero.get_hurt(1, push)

    camera.update(hero.rect)
    
    screen.fill((20, 15, 35))    # bg color i believe
    ground = pygame.Rect(0, GROUND_Y, LEVEL_WIDTH, 100)

    pygame.draw.rect(screen, (60, 50, 80), camera.apply(ground))
    for marker in markers:
        pygame.draw.rect(screen, (90, 110, 160), camera.apply(marker))
    hero.draw(screen, camera)
    if monster.is_alive():
        monster.draw(screen,camera)
    pygame.display.flip() #shows wut we just drew cus it happens in the bg where we cannot see it
    clock.tick(FPS) #loops the game 60times per second
pygame.quit()


