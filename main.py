from player import Player

hero = Player("Ava")

import pygame
pygame.init()
screen =pygame.display.set_mode((1280, 720))

pygame.display.set_caption("THE DAY THAT NEVER ENDED")
clock = pygame.time.Clock()

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    hero.update()
    screen.fill((20, 15, 35))    
    hero.draw(screen)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()