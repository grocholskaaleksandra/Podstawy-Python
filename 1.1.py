#  1.1.	Napisz skrypt, który będzie wyświetlać wszystkie kolejne dzielniki wprowadzonej liczby:

liczba = int(input("Wprowadz liczbe:"))

i = []
for i in range (1, liczba+1):
    if liczba%i == 0 :
        print (i)