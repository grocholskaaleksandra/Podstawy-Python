#utworz program do znajdowania miejsc zerowych trojmianu kwadratowego
import math
def delta (a,b,c):
    return b*b-4*a*c

decyzja = 't'
while decyzja == 't':

    print("Podaj funkcje kwadratowa a,b,b")
    a = float(input('Podaj wartosc a: '))
    b = float(input('Podaj wartosc b: '))
    c = float(input('Podaj wartosc c: '))

    if delta(a,b,c) <0:
        print("Brak miejsc zerowych")
    elif delta(a,b,c) == 0:
        print("Miejsce zerowe to:", (-b/2*a))
    else:
        print("Miejsce zerowe z1 to: ", (-b+math.sqrt(delta(a,b,c))/(2*a)))
        print("Miejsce zerowe z1 to: ", (-b-math.sqrt(delta(a,b,c))/(2*a)))

    print ("Czy powtorzyc dzialanie programu? t/n")
    decyzja = input()