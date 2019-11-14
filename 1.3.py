# 1.3.	Korzystając z pojęcia funkcji utwórz program, który będzie miał możliwość zamiany temperatury 
#pomiędzy skalami Celsjusza i Fahrenheita (w obie strony). C = (F-32)x(5/9), F = (C*9/5)+32

program = "T"
while program == "T":

    wybor = input ("Ktore przeliczenie chcesz wykonac? CnaF czy FnaC?:" )
    temperatura = float(input ("Wpisz temperature:" ))
    
    def Celcjusza_na_Farenheity (C):
        F = (C*9/5)+32
        return (F)
        
    def Farenheity_na_Celcjusza (F):
        C = (F-32)*(5/9)
        return (C)
        
    if wybor == "CnaF":
        print(round(Celcjusza_na_Farenheity(temperatura),2))
    elif wybor == "FnaC":
        print(round(Farenheity_na_Celcjusza(temperatura),2))
    else:
        print("Wpisano zla opcje")
    
    program = print(input("Czy wykonac ponownie? T/N?" ))

print("Bye bye")