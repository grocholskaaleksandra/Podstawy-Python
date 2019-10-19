#uwtorz program dodajacy ulamki zwykle


from fractions import Fraction

decyzja = 't'
while decyzja == 't':
    a = Fraction(input("Wprowadz pierwszy ulamek"))
    b = Fraction(input("Wprowadz drugi ulamek"))
    
    print(a+b)

    print ("Czy powtorzyc dzialanie programu? t/n")
    decyzja = input()