# odp = False
# print(type(odp))
#
# if odp:
#     print("Brawo")
# else:
#     print ("Porażka")

# podatek = 0.9
# zarobki = int(input("Podaj dochód"))
# if zarobki < 10000:
#     podatek =0.0
# elif zarobki < 30000:
#     podatek = 0.2
# elif zarobki <100000:
#     podatek = 0.6
# else:
#     podatek = 0.9
# print (f"Zapłacisz {zarobki * podatek} pln. (Stawka {podatek}%)")


# suma_zam = 150
# rabat = 25 if suma_zam > 150 else 0
# print(f"Rabacik {rabat}")

# alert_system = 'email'
# error = 'critical'
# error_list = []
#
# if alert_system == 'console':
#     print("Stało się coś strasznego!!!")
# elif alert_system == 'email':
#     if error == 'critical':
#         error_list.append("Krytyczny")
#     elif error == 'medium':
#         error_list.append("Ostrzeżenie")
#     else:
#         print("Inny błąd, idź na kawę.")
# else:
#     print("Nie ma takiego systemu")
#
# print(error_list)

# dobre = 0
# zle = 0
# odp = input("2x2=")
# if odp == "4":
#     print("Brawo")
#     dobre = dobre + 1
# else:
#     print("Słabo")
#     zle = zle + 1
#
# odp = input("2x3=")
# if odp == "6":
#     print("Brawo")
#     dobre = dobre + 1
# else:
#     print("Słabo")
#     zle = zle + 1
# print(f"""Wynik testu
# Dobre: {dobre}
# Złe: {zle}
# """)

# lista = []
# lang = input("Podaj znane Ci języki")
#
# match lang.lower.replace(' ',''):
#     case "java":
#         print(f"{lang}")
#     case _:
#         print('Wartość domyślna')

# for _ in range(1,3):
#     print(_)

# for i in range (10):
#     if i % 2 == 0:
#         print(i, "przysta")

# imiona = ['Radek','Asia', 'Zbyszek', 'Ala']
# a=0
# for p in imiona:
#     print(a,p, imiona.index(p))
#     a +=1

# imiona = ['Radek','Asia', 'Zbyszek', 'Ala']
# for i in range(len(imiona)):
#     print(i, imiona[i])

# iimiona = ['Radek','Asia', 'Zbyszek', 'Ala']
# # for p in enumerate(imiona):
# #     print(p)
# for p, o in enumerate(imiona):
#     print(p,o, sep='\n', end="\n\n")

# ludzie = ['Radek','Asia', 'Zbyszek', 'Ala']
# wiek = [41, 42, 43, 44]
# for x in range(len(ludzie)):
#     print(x, ludzie[x], wiek[x])

# for p,w in zip(ludzie, wiek):
#     print(p,w)

# for a, (c,d) in enumerate(zip(ludzie,wiek)):
#     print(a,c,d)


# for i in range (0,-100,-1):
#     print(i)

dictionary = {'imie':'Radek','nazwisko':"Kowalski"}
# for i in dictionary:
#     print(i)
#
# for v in dictionary.values():
#     print(v)

# for i in dictionary.items():
#     print(i)

# for j,k in dictionary.items():
#     print(j,"x",k)

c={'name':"Radek", 'age':5}
print({v:k for k,v in c.items()})
