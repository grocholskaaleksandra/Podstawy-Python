# 2.7 Utworzyć skrypt z interfejsem tekstowym obliczający symbol Newtona n po k.
# Utworzyć funkcję, która będzie wywoływać inną funkcję.

n = int(input("Wprowadz n: "))
k = int(input("Wprowadz k: "))

def silnia(cyfra):
    if cyfra == 1 or cyfra == 0:
        return 1
    wynik = cyfra * silnia(cyfra-1)
    return wynik 

def Newton (pierwsza,druga):
    if druga == 0 or druga == pierwsza:
        return 1
    elif druga>=pierwsza:
        return print ("k musi byc mniejsze od n")
    wynik = silnia(pierwsza)/(silnia(druga)*silnia(pierwsza-druga))
    return wynik

print ("Symbol Newtona n po k wynosi: ", Newton(n,k))


