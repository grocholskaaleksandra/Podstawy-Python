# 1.5 Utwórz program do znajdowania miejsc zerowych trójmianu kwadratowego x1 = (-b+sqrt(b*b-4*a*c))/(2*a) x2 = (-b-sqrt(b*b-4*a*c))/(2*a)

import math
program = "t"

while program == "t":

    a = int(input("Wprowadz a: "))
    b = int(input("Wprowadz b: "))
    c = int(input("Wprowadz c: "))
    
    delta = (b*b)-(4*a*c)
    
    if delta <0:
        print ("Brak miejsc zerowych")
    elif delta == 0.0:
        print("Jedno miejsce zerowe:", -b/2*a)
    else:
        x1= float(-b+math.sqrt(b*b-4*a*c))/(2*a)
        x2= float(-b-math.sqrt(b*b-4*a*c))/(2*a)
        print ("Pierwsze miejsce zerowe to: ", x1)
        print ("Drugie miejsce zerowe to: ", x2)
        
    program = input("Czy wykonac ponownie? t/n")

print ("Bye bye")
