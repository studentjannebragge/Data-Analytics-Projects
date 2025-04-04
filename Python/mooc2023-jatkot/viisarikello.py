import pygame
import math
import time

# Ikkunan koko
width, height = 400, 400
screen = pygame.display.set_mode((width, height))

# teksti ikkunan yläkulmaan
roomalaiset = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L'}

def muunna_roomalaiseksi(luku):
    if luku == 0:
        return ' '
    roomalainen = ''
    for arvo in sorted(roomalaiset.keys(), reverse=True):
        while luku >= arvo:
            roomalainen += roomalaiset[arvo]
            luku -= arvo
    return roomalainen

# Kellon asetukset
radius = 150
padding = 20

# Käynnistä Pygame
pygame.init()

# Käynnistä kello
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0, 0, 0))

    # Piirrä kello
    pygame.draw.circle(screen, (255, 0, 0), (width//2, height//2), radius+padding, 3)
    pygame.draw.circle(screen, (255, 0, 0), (width//2, height//2), 10)

    # Hae nykyinen aika
    t = time.localtime()
    hours = t.tm_hour
    minutes = t.tm_min
    seconds = t.tm_sec

    # Laske viisarien kulmat
    hour_angle = math.pi/2 - (hours % 12 + minutes/60) * 2*math.pi/12
    minute_angle = math.pi/2 - (minutes + seconds/60) * 2*math.pi/60
    second_angle = math.pi/2 - seconds * 2*math.pi/60

    # Piirrä viisarit
    pygame.draw.line(screen, (0, 0, 255), (width//2, height//2), (width//2 + radius*math.cos(hour_angle), height//2 - radius*math.sin(hour_angle)), 6)
    pygame.draw.line(screen, (0, 0, 100), (width//2, height//2), (width//2 + radius*math.cos(minute_angle), height//2 - radius*math.sin(minute_angle)), 4)
    pygame.draw.line(screen, (0, 0, 50), (width//2, height//2), (width//2 + radius*math.cos(second_angle), height//2 - radius*math.sin(second_angle)), 2)

    #teksti ikkunan yläkulman
    tunti = muunna_roomalaiseksi(t.tm_hour)
    minuutti = muunna_roomalaiseksi(t.tm_min)
    sekunti = muunna_roomalaiseksi(t.tm_sec)
    aika_tekstina = f"{tunti}:{minuutti}:{sekunti}"
    pygame.display.set_caption(aika_tekstina)

    #päivitetään näyttö
    pygame.display.flip()

    # Päivitä 60 kertaa sekunnissa
    clock.tick(60)

pygame.quit()
