#napisz program ktory wyswietli mnozniki wpisanej liczby i wyswietli komunikat

decyzja = 't'

while decyzja == 't':
    print("Ten program wyswietla mnozniki wpisanej liczby.")
    print("Wprowadz liczbe: ")

    liczba = round(float(input()), 1)

    for i in range(1, 11):
        print(liczba, '*', i, '=', liczba*i)

    print("Czy chcesz powtorzyc działanie programu? t/n")
    decyzja = input()