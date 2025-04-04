import tkinter as tk

class Kello:
    def __init__(self, tunnit: int, minuutit: int, sekunnit: int):
        self.sekunnit = sekunnit
        self.minuutit = minuutit
        self.tunnit = tunnit

    def tick(self):
        if self.sekunnit < 60:
            self.sekunnit += 1
        if self.sekunnit == 60:
            self.sekunnit = 0
            self.minuutit += 1
        if self.minuutit > 59:
            self.minuutit = 0
            self.sekunnit = 0
            self.tunnit += 1
        if self.tunnit > 23:
            self.minuutit = 0
            self.sekunnit = 0
            self.tunnit = 0

    def aseta(self, tunnit: int, minuutit: int):
        self.sekunnit = 0
        self.minuutit = minuutit
        self.tunnit = tunnit

    def __str__(self):
        return f'{self.tunnit:02d}:{self.minuutit:02d}:{self.sekunnit:02d}'

class KelloUI:
    def __init__(self, ikkuna):
        self.ikkuna = ikkuna
        self.kello = Kello(12, 0, 0)
        self.label = tk.Label(ikkuna, text=str(self.kello), font=("Helvetica", 48))
        self.label.pack()
        self.paivita_kello()

    def paivita_kello(self):
        self.kello.tick()
        self.label['text'] = str(self.kello)
        # Päivitä kellon aika joka sekunti (1000 millisekuntia)
        self.ikkuna.after(1000, self.paivita_kello)

if __name__ == "__main__":
    ikkuna = tk.Tk()
    ui = KelloUI(ikkuna)
    ikkuna.mainloop()
