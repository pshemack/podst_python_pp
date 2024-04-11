import random
lista = [5, 7, 4,34.56, 67, 89]
# print(random.choice(lista))

print(random.sample(lista,6))
print(random.choices(lista, k=6))
