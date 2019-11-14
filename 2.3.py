# 2.3 Utwórz skrypt z interfejsem tekstowym, który wyliczy sumę n kolejnych liczb (użytkownik podaje pierwszą i ostatnią liczbę sumy).
# Uwaga – w zadaniu należy zbudować funkcję własną realizującą dane zadanie.

program = "t"
while program =="t":

    def dodawanie (pierwsza, ostatnia):
        for i in range(pierwsza, ostatnia):
            obliczenie = pierwsza + i+1
            pierwsza = obliczenie
        return(obliczenie)
    
    pierwsza_liczba = int(input("Wprowadz pierwsza liczbe: "))
    ostatnia_liczba = int(input("Wprowadz druga liczbe: "))
    
    print(dodawanie(pierwsza_liczba, ostatnia_liczba))

    program = input("Czy wykonac ponownie? t/n ")
    
print ("Bye bye")
