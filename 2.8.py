# 2.8 Utworzyć skrypt z interfejsem tekstowym, który będzie zwracać wiersz n-tego rzędu z trójkąta Pascala 
# (użytkownik podaje n, program zwraca odpowiadający wiersz trójkąta).

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

n = int(input ("Wprowadz n-ty rzad trojkatu Pascala: " ))

def trojkat (wiersz):
    lista = []
    for i in range (wiersz+1):
        for j in range (i+1):
            newton = int(Newton(i,j))
            lista.append(newton)
        print (lista)
        lista.clear()


trojkat(n)