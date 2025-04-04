import pygame
import random

pygame.init()

#robotti, robotin ilmestymen ja ajastin
robo_tiedosto = pygame.image.load("robo.png")
robo_leveys = robo_tiedosto.get_width()
robo_korkeus = robo_tiedosto.get_height()
kello = pygame.time.Clock()
uusi_robo = pygame.USEREVENT + 1
aika =  random.randint(500, 2500)
ajastin = pygame.time.set_timer(uusi_robo, aika)


#näyttöasetukset
ikkunan_leveys = 640
ikkunan_korkeus = 480
naytto = pygame.display.set_mode((ikkunan_leveys, ikkunan_korkeus))


# Luo lista robotteja varten
robotit = []

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == uusi_robo:
            x = random.randint(0, ikkunan_leveys - robo_leveys)
            y = -robo_korkeus
            nopeus_x, nopeus_y = 0, 4
            suunta = random.choice([-4 , 4])
            robotit.append([x, y, nopeus_x, nopeus_y, suunta])
            
            # Päivitä ajastimen aikaväli
            aika = random.randint(500, 2000)
            pygame.time.set_timer(uusi_robo, aika)
    
    naytto.fill((0,0,0))
    
    # Piirrä kaikki robotit ja päivitä niiden sijainnit
    for robo in robotit:
        x, y, nopeus_x, nopeus_y, suunta = robo
        naytto.blit(robo_tiedosto, (x, y))
        robo[0] += nopeus_x
        robo[1] += nopeus_y

        # Käännä robo, kun se osuu ikkunan pohjaan
        if y + robo_korkeus > ikkunan_korkeus:
            robo[3] = 0
            robo[2] = suunta

    pygame.display.flip()
    kello.tick(60)

pygame.quit()