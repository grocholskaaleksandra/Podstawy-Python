# 2.4 Utwórz skrypt z interfejsem tekstowym, który przyjmie od użytkownika ile elementów chce on wprowadzić do listy,
# przyjmie te elementy, a następnie wyliczy: średnią i odchylenie standardowe średniej. 
#Wykonać zadanie na dwa sposoby: poprzez utworzenie funkcji własnych obliczających średnią i odchylenie standardowe 
#oraz korzystając z gotowych funkcji np. z pakietu numpy.

import numpy
import math

ilosc_elementow = int(input("Ile elementow chcesz wprowadzic? "))
lista = []

for i in range (ilosc_elementow):
    element = int(input("Wprowadz element: "))
    lista.append (element)
    
    
def srednia (elementy):
    wynik = sum(elementy)/len(elementy)
    return wynik

print (srednia(lista))

srednia_numpy = numpy.mean(lista)
print (srednia_numpy)


def odchylenie (elementy):
    dystans = []
    for i in range (len(elementy)):
        zmienne = ((elementy[i]-(sum(elementy)/len(elementy)))**2)
        dystans.append (zmienne)
    wynik = math.sqrt(sum(dystans)/len(elementy))
    return (wynik)
print (odchylenie(lista))
    
odchylenie_numpy = numpy.std(lista)
print (odchylenie_numpy)
