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
