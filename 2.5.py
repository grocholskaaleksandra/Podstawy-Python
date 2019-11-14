# 2.5 Utwórz skrypt z interfejsem tekstowym który obliczy silnię od danego argumentu. 
#Wykonać zadanie na dwa sposoby – iteracyjnie i rekurencyjnie.

argument = int(input("Wprowadz liczbe do obliczenia silni: "))

liczba = 1
for i in range (1, argument):
    obliczenia = liczba*(i+1)
    liczba = obliczenia
    
print (obliczenia)

def silnia (numer):
    if numer ==1:
        return 1 
    return numer *silnia(numer-1)
    
print (silnia(argument))

