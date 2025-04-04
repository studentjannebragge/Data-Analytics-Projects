import pygame
import random

pygame.init()
naytto = pygame.display.set_mode((640, 480))

robo = pygame.image.load("robo.png")

robo_leveys = robo.get_width()
robo_korkeus = robo.get_height()

robo_x = random.randint(0, 640 - robo_leveys)
robo_y = random.randint(0, 480 - robo_korkeus)

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.MOUSEBUTTONDOWN:
            if robo_x <= tapahtuma.pos[0] <= robo_x + robo_leveys and robo_y <= tapahtuma.pos[1] <= robo_y + robo_korkeus:
                robo_x = random.randint(0, 640 - robo_leveys)
                robo_y = random.randint(0, 480 - robo_korkeus)

        

        if tapahtuma.type == pygame.QUIT:
            exit()
            
    naytto.fill((0, 0, 0))
    naytto.blit(robo, (robo_x, robo_y))
    pygame.display.flip()