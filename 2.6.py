# 2.6 Utworzyć skrypt z interfejsem tekstowym obliczający n-ty element ciągu Fibonacciego –
# wykonać zadanie iteracyjnie i rekurencyjnie. 

nty = int(input("Wprowadz ktory element ciagu chcesz obliczyc: "))

pierwszy = 1 
drugi = 2
for i in range (nty-3): 
    wynik = pierwszy+drugi
    pierwszy = drugi 
    drugi = wynik
print (wynik)

def ciag (Fn):
    if (Fn-1) ==1:
        return 1 
    elif (Fn-2) ==1:
        return 1
    return ciag(Fn-1)+ciag(Fn-2)
    
print (ciag(nty+1))
