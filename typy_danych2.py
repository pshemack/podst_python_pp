lista = []
print(type(lista))


lista.append("R1")
lista.append("R2")
lista.append("R3")
lista.append("t1")
lista.append(6)
print(lista)
print(len(lista))
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[-1])

print(lista[3:])
lista[2]="Miko"
print(lista)
indeks = lista.index(6)
print(lista.pop(4))
print(lista)

lista2=lista
lista3=lista.copy()
lista.clear()
print("L1", lista)
print("L2", lista2)
print("L3", lista3)

liczby = [54, 999, 34, 22, 64.34, 687]
print(liczby)
liczby.sort()
print(liczby)

osoby=["radek", "ola", "kasia"]
print(osoby)
osoby.sort()
print(osoby)

krotka = tuple(lista3)
print(krotka)