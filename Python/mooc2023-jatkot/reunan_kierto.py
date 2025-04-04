import pygame

pygame.init()
naytto = pygame.display.set_mode((640, 480))

robo = pygame.image.load("robo.png")

x = 0
y = 0
xnopeus = 1
ynopeus = 0
kello = pygame.time.Clock()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()

    naytto.fill((0, 0, 0))
    naytto.blit(robo, (x, y))
    pygame.display.flip()
    
    x += xnopeus
    y += ynopeus
    
    if xnopeus > 0 and x+robo.get_width() >= 640:
        xnopeus = 0
        ynopeus = 1
    
    
    if ynopeus > 0 and y+robo.get_height() >= 480:
        ynopeus = 0
        xnopeus = -1
    
    if xnopeus < 0 and x <= 0:
        xnopeus = 0
        ynopeus = -1
    
    if ynopeus < 0 and y <= 0:
        ynopeus = 0
        xnopeus = 1
        

    kello.tick(60)