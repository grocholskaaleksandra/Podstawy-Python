#Utworz program ktory bedzie komunikowac czy wprowadzona liczba jest dodatnia czy nie

decyzja = 't'

while decyzja == 't':

    x = float(input("Wprowadz liczbe"))

    if x > 0:
        print("Liczba jest dodatnia")
    elif x == 0:
        print("Liczba jest zerem")
    else:
        print("Liczba jest ujemna")

    decyzja = input("Czy wykonac ponownie t/n?")