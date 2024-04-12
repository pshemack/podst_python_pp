class Human:
    """
    Klasa Human opisująca człowieka w python
    """
    imie = ""
    wiek = None
    plec = "k"

    def powitanie(self):
        print(f"Nazywam się {self.imie}")


# print(Human.__doc__)
# print(print.__doc__)

cz1 = Human()
cz1.imie = "Anna"
cz1.wiek = 56

print(cz1)
print(cz1.imie)
print(cz1.wiek)
print(cz1.plec)

cz2 = Human()
cz2.imie = "Adam"
cz2.wiek = 46
cz2.plec = "m"
print(cz2)
print(cz2.imie)
print(cz2.wiek)
print(cz2.plec)

cz1.powitanie()
cz2.powitanie()
