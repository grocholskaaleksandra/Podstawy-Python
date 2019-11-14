# 1.2.	Korzystając z pętli for oraz możliwości formatowania działania funkcji print utwórz program, 
#który po prowadzeniu liczby wyświetli następujący komunikat:
#
#Enter a number : 5 <- liczba wprowadzona przez uzytkownika
#5.0 x 1 = 5.0
#5.0 x 2 = 10.0
#5.0 x 3 = 15.0
#5.0 x 4 = 20.0
#5.0 x 5 = 25.0
#5.0 x 6 = 30.0
#5.0 x 7 = 35.0
#5.0 x 8 = 40.0
#5.0 x 9 = 45.0
#5.0 x 10 = 50.0



liczba = float(input("Enter a number:"))

for i in range (1,11):
    print (liczba, "x", i, "=", liczba*i)