# 1.6.	Utwórz program, który będzie komunikować, czy wprowadzona liczba jest dodatnia czy nie

program = "t"
while program == "t":
    liczba = float(input("Wprowadz liczbe: " ))
    
    if liczba < 0:
        print ("Liczba jest ujemna")
    elif liczba == 0: 
        print ("Liczba jest zerem")
    else: 
        print ("Liczba jest dodatnia")
        
    program = input("Czy wykonac ponownie? t/n ")

print ("Bye bye")
