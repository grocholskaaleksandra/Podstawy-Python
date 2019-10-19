#Korzystajac z pojecia funkcji napisz program ktory bedzie mial mozliwosc zmiany temp pomiedzy C a F
def FnaC (F):
    print(F, "Farnehaitow na stopnie Celciusza to:", (F-32)*(5/9))
    return
def CnaF (C):
    return (C*9/5)+32

decyzja = 't'
while decyzja == 't':

    print("Wybierz przeliczenie: FnaC czy CnaF?")

    wybor = str(input())
    if wybor == 'FnaC':
        print("Wpisz temperature:")
        F = float(input())
        FnaC(F)
    elif wybor == 'CnaF':
        print("Wpisz temperature:")
        C = float(input())
        CnaF(C)
        print(C, "Celcjuszy na stopnie Farenhaita to:", CnaF(C))
    else:
        print("Bledny wybor")

    print("Czy wykonac ponownie t/n?")
    decyzja = (input())
