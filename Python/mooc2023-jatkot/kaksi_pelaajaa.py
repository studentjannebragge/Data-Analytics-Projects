import pygame

pygame.init()
naytto = pygame.display.set_mode((640, 480))

class Robotti:
    def __init__(self, kuva, ohjaus, aloituspaikka):
        self.kuva = pygame.image.load(kuva)
        self.x, self.y = aloituspaikka
        self.ohjaus = ohjaus
        self.liike = {"oikealle": False, "vasemmalle": False, "ylos": False, "alas": False}

    def liiku(self):
        if self.liike["oikealle"]:
            self.x += 2
            if self.x + self.kuva.get_width() >= 640:
                self.x -= 2
        if self.liike["vasemmalle"]:
            self.x -= 2
            if self.x <= 0:
                self.x += 2
        if self.liike["ylos"]:
            self.y -= 2
            if self.y <= 0:
                self.y += 2
        if self.liike["alas"]:
            self.y += 2
            if self.y + self.kuva.get_height() >= 480:
                self.y -= 2

    def piirra(self, naytto):
        naytto.blit(self.kuva, (self.x, self.y))

robo1 = Robotti("robo.png", {"oikealle": pygame.K_RIGHT, "vasemmalle": pygame.K_LEFT, "ylos": pygame.K_UP, "alas": pygame.K_DOWN}, (0, 480 - pygame.image.load("robo.png").get_height()))
robo2 = Robotti("robo.png", {"oikealle": pygame.K_d, "vasemmalle": pygame.K_a, "ylos": pygame.K_w, "alas": pygame.K_s}, (640 - pygame.image.load("robo.png").get_width(), 0))

kello = pygame.time.Clock()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.KEYDOWN:
            for robo in [robo1, robo2]:
                if tapahtuma.key == robo.ohjaus["oikealle"]:
                    robo.liike["oikealle"] = True
                if tapahtuma.key == robo.ohjaus["vasemmalle"]:
                    robo.liike["vasemmalle"] = True
                if tapahtuma.key == robo.ohjaus["ylos"]:
                    robo.liike["ylos"] = True
                if tapahtuma.key == robo.ohjaus["alas"]:
                    robo.liike["alas"] = True

        if tapahtuma.type == pygame.KEYUP:
            for robo in [robo1, robo2]:
                if tapahtuma.key == robo.ohjaus["oikealle"]:
                    robo.liike["oikealle"] = False
                if tapahtuma.key == robo.ohjaus["vasemmalle"]:
                    robo.liike["vasemmalle"] = False
                if tapahtuma.key == robo.ohjaus["ylos"]:
                    robo.liike["ylos"] = False
                if tapahtuma.key == robo.ohjaus["alas"]:
                    robo.liike["alas"] = False

        if tapahtuma.type == pygame.QUIT:
            exit()

    for robo in [robo1, robo2]:
        robo.liiku()

    naytto.fill((0, 0, 0))

    for robo in [robo1, robo2]:
        robo.piirra(naytto)

    pygame.display.flip()

    kello.tick(60)


