import pygame

pygame.init()
naytto = pygame.display.set_mode((640, 480))

robo = pygame.image.load("robo.png")

naytto.fill((0,0,0))

leveys = robo.get_width()
korkeus = robo.get_height()



for i in range(11):
    if i == 0:
        continue
    else:
        naytto.blit(robo, (leveys * i, korkeus))



pygame.display.flip()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()
