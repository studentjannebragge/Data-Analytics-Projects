import pygame

pygame.init()

# Määritä ikkunan koko
ikkunan_leveys = 640
ikkunan_korkeus = 480
naytto = pygame.display.set_mode((ikkunan_leveys, ikkunan_korkeus))
kello = pygame.time.Clock()

pallo = pygame.image.load("pallo.png")

# Määritä pallon koko
pallo_leveys = pallo.get_width()
pallo_korkeus = pallo.get_height()

# Määritä pallon sijainti ja nopeus
x, y = 0, 0
nopeus_x, nopeus_y = 2, 2

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    naytto.fill((0,0,0))

    # Piirrä pallo ja päivitä sen sijainti
    naytto.blit(pallo, (x, y))
    x += nopeus_x
    y += nopeus_y

    # Käännä pallo, kun se osuu ikkunan reunaan
    if x + pallo_leveys > ikkunan_leveys or x < 0:
        nopeus_x = -nopeus_x
    if y + pallo_korkeus > ikkunan_korkeus or y < 0:
        nopeus_y = -nopeus_y

    pygame.display.flip()
    kello.tick(60)

pygame.quit()