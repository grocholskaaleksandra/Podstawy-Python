# 1.4.	Utwórz program do zamiany kilometrów na mile i na odwrót.

program = "t"
while program == "t":

    wybor = input("Ktore przeliczenie wykonac? KnaM czy MnaK? ")
    odleglosc = float(input("Wprowadz wartosc: "))
    
    def Kilomerty_na_Mile (K):
        K = (K/1.609344)
        return (K)
        
    def Mile_Na_Kilometry (M):
        M = (M*1.609344)
        return (M)
        
    if wybor == "KnaM":
        print(round(Kilomerty_na_Mile(odleglosc),2))
    elif wybor == "MnaK":
        print(round(Mile_Na_Kilometry(odleglosc),2))
    else: 
        print ("Wybrano zle przeliczenie")
        
    program = input("Czy uruchomic ponownie? t/n")

print ("Bye bye")
