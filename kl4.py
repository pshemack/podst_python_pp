class Dom:
    """
    Klasa Dom
    """


    def __init__(self, metraz, kolor, liczba_okien):
        self.metraz = metraz
        self.kolor = kolor
        self.__liczba_okien = 0

    def dodaj_okno(self):
        self.__liczba_okien += 1

    def liczba_okien(self):
        print(f"Liczba okien wynosi {self.__liczba_okien}.")

d1 = Dom(240,"biały",3)
d1.liczba_okien()
d1.dodaj_okno()
d1.liczba_okien()