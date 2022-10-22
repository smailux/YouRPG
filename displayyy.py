import pygame
import random
import json


pygame.init()
black = (0, 0, 0)
screen = pygame.display.set_mode((800, 600))

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

    pygame.display.flip()
    screen.fill('white')

    myFont = pygame.font.SysFont("Times New Roman", 18)
    stats = json.load(open('variu.json', 'r+'))

    J1_stats = myFont.render(
        f'Name : {stats[0]}, PV : {stats[1]}, PM : {stats[2]}, Speed : {stats[3]}, Money : {stats[4]}.', True, black)
    J2_stats = myFont.render(
        f'Name : {stats[5]}, PV : {stats[6]}, PM : {stats[7]}, Speed : {stats[8]}, Money : {stats[9]}.', True, black)

    screen.blit(J1_stats, (20, 10))
    screen.blit(J2_stats, (20, 50))
