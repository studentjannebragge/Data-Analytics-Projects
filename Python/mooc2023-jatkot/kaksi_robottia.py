import pygame

pygame.init()
naytto = pygame.display.set_mode((640, 480))

robo = pygame.image.load("robo.png")
robo2 = pygame.image.load("robo.png")

x = 0
x2 = 0
y = 0
y2 = 0

nopeus = 1
nopeus2 = 1

kello = pygame.time.Clock()

robo_leveys = robo.get_width()
robo_korkeus = robo.get_height()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()
            
            
    x += nopeus
    x2 += nopeus2 * 2
    
    naytto.fill((0, 0, 0))
    naytto.blit(robo, (x, y + robo_korkeus / 2))
    if nopeus > 0 and x+robo.get_width() >= 640:
        nopeus = -nopeus
    if nopeus < 0 and x <= 0:
        nopeus = -nopeus
    
    naytto.blit(robo2, (x2, y2 + robo_korkeus * 1.6))
    if nopeus2 > 0 and x2+robo2.get_width() >= 640:
        nopeus2 = -nopeus2
    if nopeus2 < 0 and x2 <= 0:
        nopeus2 = -nopeus2
    
    
    
    pygame.display.flip()
    
   
    if nopeus > 0 and x+robo.get_width() >= 640:
        nopeus = -nopeus
    if nopeus < 0 and x <= 0:
        nopeus = -nopeus

    kello.tick(60)
