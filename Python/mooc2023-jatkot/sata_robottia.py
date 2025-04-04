import pygame

pygame.init()
naytto = pygame.display.set_mode((640, 480))

robo = pygame.image.load("robo.png")

naytto.fill((0,0,0))

robo_leveys = robo.get_width()
robo_korkeus = robo.get_height()



for i in range(10):
    for j in range(10):
        x = i * robo_leveys + j * robo_leveys / 7
        y = j * robo_korkeus / 4
        naytto.blit(robo, (robo_leveys + x, robo_korkeus + y))



pygame.display.flip()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()

