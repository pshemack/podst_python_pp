# while True
#
# try:
#     z1=float(input("Zmienna1:"))
#     d=input("Działanie(/*):")
#     z2=float(input("Zmienna2:"))
#
#     match d:
#         case "*":
#             print(z1*z2)
#         case "/":
#             print(z1/z2)
#
# except ZeroDivisionError as e:
#     print("Nie dziel przez zero",e)

while True:
    odp = input("Podaj wyrażenie")
    print(eval(odp))
