import pygame
import sys

class Ristinolla:
    def __init__(self):
        self.RUUDUKKO = [[None, None, None] for _ in range(3)]
        self.PELAAJA = 'X'
        self.VOITTAJA = None

    def vaihda_pelaajaa(self):
        self.PELAAJA = 'O' if self.PELAAJA == 'X' else 'X'

    def tarkista_voittaja(self):
        # tarkista rivit
        for rivi in self.RUUDUKKO:
            if rivi.count(rivi[0]) == len(rivi) and rivi[0] is not None:
                self.VOITTAJA = rivi[0]
                return

        # tarkista sarakkeet
        for sarake in range(len(self.RUUDUKKO)):
            if self.RUUDUKKO[0][sarake] == self.RUUDUKKO[1][sarake] == self.RUUDUKKO[2][sarake] and self.RUUDUKKO[0][sarake] is not None:
                self.VOITTAJA = self.RUUDUKKO[0][sarake]
                return

        # tarkista diagonaalit
        if self.RUUDUKKO[0][0] == self.RUUDUKKO[1][1] == self.RUUDUKKO[2][2] and self.RUUDUKKO[0][0] is not None:
            self.VOITTAJA = self.RUUDUKKO[0][0]
            return
        if self.RUUDUKKO[0][2] == self.RUUDUKKO[1][1] == self.RUUDUKKO[2][0] and self.RUUDUKKO[0][2] is not None:
            self.VOITTAJA = self.RUUDUKKO[0][2]
            return

        # tarkista tasapeli
        if all([all(rivi) for rivi in self.RUUDUKKO]):
            self.VOITTAJA = 'Tasapeli'
            return

    def piirra_ruudukko(self):
        for rivi in range(3):
            for sarake in range(3):
                if self.RUUDUKKO[rivi][sarake] == 'X':
                    pygame.draw.line(screen, (255, 255, 255), (sarake * 200 + 50, rivi * 200 + 50), (sarake * 200 + 150, rivi * 200 + 150), 2)
                    pygame.draw.line(screen, (255, 255, 255), (sarake * 200 + 150, rivi * 200 + 50), (sarake * 200 + 50, rivi * 200 + 150), 2)
                elif self.RUUDUKKO[rivi][sarake] == 'O':
                    pygame.draw.circle(screen, (255, 255, 255), (sarake * 200 + 100, rivi * 200 + 100), 50, 2)

    def pelaa(self, x, y):
        if self.RUUDUKKO[y][x] is None:
            self.RUUDUKKO[y][x] = self.PELAAJA
            self.tarkista_voittaja()
            self.vaihda_pelaajaa()

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Ristinolla')
font = pygame.font.Font(None, 48)
ristinolla = Ristinolla()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and ristinolla.VOITTAJA is None:
            mouseX = event.pos[0] // 200
            mouseY = event.pos[1] // 200
            ristinolla.pelaa(mouseX, mouseY)

    screen.fill((0, 0, 0))

    # piirrä ruudukko
    for i in range(1, 3):
        pygame.draw.line(screen, (255, 255, 255), (0, i * 200), (600, i * 200), 2)
        pygame.draw.line(screen, (255, 255, 255), (i * 200, 0), (i * 200, 600), 2)

    ristinolla.piirra_ruudukko()

    # näytä voittaja
    if ristinolla.VOITTAJA:
        text = font.render(ristinolla.VOITTAJA + ' voitti!', True, (255, 255, 255))
        screen.blit(text, (200, 300))

    pygame.display.update()
