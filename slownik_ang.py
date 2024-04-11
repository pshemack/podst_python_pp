slownik = {"dom":"house", "house":"dom"}
print("Słówka w słowniku", slownik.keys())
pl = input("podaj pl")
print(slownik[pl.lower().replace(" ","")])
