def alkuluvut():

    def on_alkuluku(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    n = 2
    while True:
        if on_alkuluku(n):
            yield n
        n += 1


if __name__ == "__main__":
    
    luvut = alkuluvut()
    
    
    for i in range(8):
        print(next(luvut))