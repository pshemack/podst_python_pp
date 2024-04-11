import sys

print("Cześć, to ja!")
print(39)
print(type(39))
print(sys.int_info)
tekst="Witaj w świecie"
print(tekst.lower())
tekst=tekst.lower()
print(tekst.removeprefix("witaj "))
encoded_s = tekst.encode("utf-8")
print (encoded_s)
print(type(encoded_s))
print(encoded_s.decode('utf-8'))

imie="Przemek"
tekst_format = f"\tMam na imię {imie}\n i lubię Pytona.\b Dodatkowe zdanie."
print(tekst_format)

starszy = "Witaj %s!"
print(starszy % imie)

print("Witaj {}!".format(imie))

print("""
    Tekst wielolininjkowy
    dodstkowe zdanie
""")

print("%.f" % 3.9)
liczba=1234567890123
print(liczba)
print("Nasza duża liczba {:,}".format(liczba))
print(f"Nasza duża liczba {liczba:,}".replace(","," "))


temp = 36.6
temp2 = 36, 6

print(temp)
print(type(temp))

print(temp2)
print(type(temp2))

print(1+2)
print (0.1 + 0.2)
print(sys.float_info)

wyn = 0.2 + 0.7
print(f"Wynik: {wyn:.2f}")
print(f"Wynik: {wyn}")

czy_znasz_python = True
print(czy_znasz_python)
print(type(czy_znasz_python))

a = 6
b = 9
print(f"Porównanie {a} > {b}", a > b)
print(f"Porównanie {a} == {b}", a == b)
print(f"Porównanie {a} != {b}", a != b)






