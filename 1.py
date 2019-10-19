#napisz skrypt ktor bedzie wyswietlal kolejne dzielniki wyswietlonej liczby

decyzja = 't'

while decyzja == 't':
    print("Ten program podaje dzielniki podanej liczby calkowitej")
    print("Podaj liczbe")

    liczba = int(input())

    for i in range(2,liczba +1):
        if(liczba%i == 0):
            print(i)

    print ("Czy chcesz powtórzyc działanie programu t/n")
    decyzja = input()

