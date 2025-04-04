import pygame
import math

pygame.init()

# Määritä ikkunan koko
ikkunan_leveys = 640
ikkunan_korkeus = 480
naytto = pygame.display.set_mode((ikkunan_leveys, ikkunan_korkeus))

robo = pygame.image.load("robo.png")

# Määritä robotin koko
robo_leveys = robo.get_width()
robo_korkeus = robo.get_height()

# Määritä piirileikin keskipiste ja säde
keskipiste = (ikkunan_leveys / 2, ikkunan_korkeus / 2)
sade = 150

# Määritä robotin nopeus
nopeus = 0.0005

kulma = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    naytto.fill((0,0,0))

    # Piirrä kymmenen robottia piirileikissä
    for i in range(10):
        x = keskipiste[0] + sade * math.cos(kulma + i * 2 * math.pi / 10) - robo_leveys / 2
        y = keskipiste[1] + sade * math.sin(kulma + i * 2 * math.pi / 10) - robo_korkeus / 2
        naytto.blit(robo, (x, y))

    kulma += nopeus

    pygame.display.flip()

pygame.quit()
