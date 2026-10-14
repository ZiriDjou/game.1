import pygame
import random

pygame.init()


screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Shooting Monster Game")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
BLUE = (0, 100, 255)


player_x = 50
player_y = 220
player_speed = 5


monster_x = 700
monster_y = 220
monster_speed = 3


bullets = []
bullet_speed = 10


shoot_delay = 150
last_shot = 0

score = 0


clock = pygame.time.Clock()

running = True

while running:

   
    current_time = pygame.time.get_ticks()

   
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    
    keys = pygame.key.get_pressed()

    
    if keys[pygame.K_UP]:
        player_y -= player_speed

    
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    
    if player_y < 0:
        player_y = 0

    if player_y > 470:
        player_y = 470

    
    if keys[pygame.K_SPACE]:

        if current_time - last_shot > shoot_delay:

            bullets.append([
                player_x + 40,
                player_y + 15
            ])

            last_shot = current_time

    
    monster_y += monster_speed

    
    if monster_y <= 0 or monster_y >= 470:
        monster_speed = -monster_speed

    
    for bullet in bullets:
        bullet[0] += bullet_speed

    
    for bullet in bullets[:]:

        
        if bullet[0] > 800:
            bullets.remove(bullet)
            continue

        
        if (
            bullet[0] + 10 > monster_x
            and bullet[0] < monster_x + 40
            and bullet[1] + 5 > monster_y
            and bullet[1] < monster_y + 30
        ):

            score += 1

            
            bullets.remove(bullet)

            
            monster_y = random.randint(0, 470)

    
    screen.fill(WHITE)

    
    pygame.draw.rect(
        screen,
        BLUE,
        (player_x, player_y, 40, 30)
    )

    
    pygame.draw.rect(
        screen,
        RED,
        (monster_x, monster_y, 40, 30)
    )

    
    for bullet in bullets:

        pygame.draw.rect(
            screen,
            BLACK,
            (bullet[0], bullet[1], 10, 5)
        )

    
    font = pygame.font.Font(None, 36)

    text = font.render(
        "Score: " + str(score),
        True,
        BLACK
    )

    screen.blit(text, (10, 10))

    
    pygame.display.update()

    
    clock.tick(60)

pygame.quit()