import tkinter as tk

class Lahja:
    def __init__(self, nimi: str, paino: int):
        self.nimi = nimi
        self.paino = paino

    def __str__(self):
        return f'{self.nimi} ({self.paino} kg)'

class Pakkaus:
    def __init__(self):
        self.lahjat = []

    def lisaa_lahja(self, lahja: Lahja):
        self.lahjat.append(lahja)

    def yhteispaino(self):
        return sum(lahja.paino for lahja in self.lahjat)

class LahjaUI:
    def __init__(self, ikkuna):
        self.ikkuna = ikkuna
        self.pakkaus = Pakkaus()
        
        self.label = tk.Label(ikkuna, text="Lisää lahja", font=("Helvetica", 16))
        self.label.pack()

        self.nimi_entry = tk.Entry(ikkuna)
        self.nimi_entry.pack()
        
        self.paino_entry = tk.Entry(ikkuna)
        self.paino_entry.pack()

        self.button = tk.Button(ikkuna, text="Lisää", command=self.lisaa_lahja)
        self.button.pack()

        self.yhteispaino_label = tk.Label(ikkuna, text="Yhteispaino: 0 kg", font=("Helvetica", 16))
        self.yhteispaino_label.pack()

    def lisaa_lahja(self):
        nimi = self.nimi_entry.get()
        paino = int(self.paino_entry.get())
        
        lahja = Lahja(nimi, paino)
        self.pakkaus.lisaa_lahja(lahja)

        self.yhteispaino_label['text'] = f"Yhteispaino: {self.pakkaus.yhteispaino()} kg"

if __name__ == "__main__":
    ikkuna = tk.Tk()
    ui = LahjaUI(ikkuna)
    ikkuna.mainloop()
