# 2.2 W klasie przeprowadzono sprawdzian, za który uczniowie mogli otrzymać maksymalnie 40 punktów. 
#Skala ocen w szkole jest następująca: 0-39% - ndst, 40-49% - dop, 50-69% - dst, 70-84% - db, 85-99% - bdb, 100% - cel.  
#Utwórz skrypt z interfejsem tekstowym, który na podstawie podanej liczby punktów ze sprawdzianu wyświetli ocenę jaka się należy  
#(skorzystaj z konstrukcji if, elif, else). 

program = "t"
while program =="t":
    
    punkty = float(input("Wprowadz liczbe punktow: "))
    
    wynik =  punkty/40*100 
    
    if wynik <40:  
        print ("Ocena niedostateczna")
    elif wynik >=40 and wynik <50:  
        print ("Ocena dopuszczajaca")
    elif wynik >=50 and wynik <70:  
        print ("Ocena dostateczna")
    elif wynik >=70 and wynik <85:  
        print ("Ocena dobra")
    elif wynik >=85 and wynik <99:  
        print ("Ocena bardzo dobra")
    else: 
        print ("Ocena celujaca")
        
    program = input("Czy wykonac ponownie? t/n ")
    
print("Bye bye")
