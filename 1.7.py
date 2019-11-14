# 1.7.	Utwórz program dodający ułamki zwykłe

from fractions import Fraction

program = "t"
while program =="t":
    
    ulamek_pierwszy = Fraction(input("Wprowadz pierwszy ulamek: "))
    ulamek_drugi = Fraction(input("Wprowadz drugi ulamek: "))
    
    wynik = ulamek_pierwszy+ulamek_drugi
    
    print (wynik)
    
    program = input("Czy wykonac ponownie? t/n ")
    
print ("Bye bye")
