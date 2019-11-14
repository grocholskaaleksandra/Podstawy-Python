# 2.1 Utwórz skrypt z interfejsem tekstowym, który pobierze od użytkownika zdanie i wyświetli w kolejnych wierszach
# litery tego zdania w odwróconej kolejności.


zdanie = input("Wprowadz zdanie: ")

for i in zdanie[::-1]:
    print (i)
    
    

