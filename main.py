import random

import pygame


pygame.init()

#Game constants
white = (255, 255, 255)
black = (0, 0, 0)
gray = (128, 128, 128)
WIDTH = 400
HEIGHT = 500
background = white
player = pygame.transform.scale(pygame.image.load('zues.png'), (90, 70))
fps = 60
font = pygame.font.font('freesansbold.ttf', 16)
timer = pygame.time.Clock()
score = 0
high_score = 0
game_over = False


# Game variables
# actual line 78 but line 25 rn till we get rest of content
for i in range(len(platforms)):
    block = pygame.draw.rect(screen, black, platforms[i, 0, 3])
    block.append(block)

for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_a:
            x_change = -player_speed
        if event.key == pygame.K_d:
            x_change = player_speed
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_a:
            x_change = 0
        if event.key == pygame.K_d:
            x_change = 0

jump = check_collisions(blocks, jump)
player_x += x_change
player_y = update_player(player_y)
platforms = update_platforms(platforms, player_y, y_change)

if x_change > 0:
    player = pygame.transform.scale(pygame.image.load('doodle.png'), (90, 70))
elif x_change < 0:
    player = pygame.transform.flip(pygame.transform.scale(pygame.image.load('doodle.png'), (90, 70)), 1, 0)


pygame.display.flip()
pygame.quit()
