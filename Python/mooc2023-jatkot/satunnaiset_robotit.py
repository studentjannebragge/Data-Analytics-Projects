import pygame
import random

pygame.init()

ikkunan_leveys = 640
ikkunan_korkeus = 480

robo = pygame.image.load("robo.png")
robo_leveys = robo.get_width()
robo_korkeus = robo.get_height()

naytto = pygame.display.set_mode((ikkunan_leveys, ikkunan_korkeus))


naytto.fill((0,0,0))


for i in range(1000):
    x = random.randint(0, ikkunan_leveys - robo_leveys)
    y = random.randint(0, ikkunan_korkeus - robo_korkeus)
    naytto.blit(robo, (x, y))


pygame.display.flip()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()
