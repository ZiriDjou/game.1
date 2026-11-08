from player import Player

hero = Player("Ava")

import pygame
pygame.init()
screen =pygame.display.set_mode((1280, 720)) # making the window screen and its size

pygame.display.set_caption("THE DAY THAT NEVER ENDED") #name of the game
clock = pygame.time.Clock() #honestly wallah idk

running=True #initialize to true so it starts
while running: # main loop
    for event in pygame.event.get():
        if event.type==pygame.QUIT: # the X button top right
            running=False
    hero.update()
    screen.fill((20, 15, 35))    # bg color i believe
    hero.draw(screen)
    pygame.display.flip() #shows wut we just drew cus it happens in the bg where we cannot see it
    clock.tick(60) #loops the game 60times per second
pygame.quit()