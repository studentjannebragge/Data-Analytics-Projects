class Aanite:
    def __init__(self, pituus: int):
        if pituus > 0:
            self.__pituus = pituus
        else:
            raise ValueError("Pituus ei voi olla alle nollan!")
        
    @property
    def pituus(self):
        return self.__pituus
    
    @pituus.setter
    def pituus(self, pituus):
        if pituus > 0:
            self.__pituus = pituus
        else:
            raise ValueError("Pituus ei voi olla alle nollan!")


if __name__ == "__main__":
    the_wall = Aanite(-43)
    print(the_wall.pituus)
    the_wall.pituus = 44
    print(the_wall.pituus)