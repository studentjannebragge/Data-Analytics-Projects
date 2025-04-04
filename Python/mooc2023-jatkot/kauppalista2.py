class Kauppalista:
    def __init__(self, tuotteet):
        self.tuotteet = tuotteet
        self.indeksi = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.indeksi < len(self.tuotteet):
            tuote = self.tuotteet[self.indeksi]
            self.indeksi += 1
            return tuote
        else:
            raise StopIteration

if __name__ == "__main__":
    kauppalista = Kauppalista(["omena", "banaani", "maito", "leipä"])
    iteraattori = iter(kauppalista)

    while True:
        try:
            tuote = next(iteraattori)
            print(tuote)
        except StopIteration:
            break
