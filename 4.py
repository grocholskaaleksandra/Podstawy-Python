#utworz program do zmiany kilometrow na mile i na odwrot

def MnaKM (M):
    return M*1.609
def KMnaM (KM):
    return KM/1.609

decyzja = 't'
while decyzja == 't':

    print('Wybierz przeliczenie MnaKM albo KMnaM')
    wybor = input()

    if wybor == 'MnaKM':
        print('Wpisz odleglosc:')
        M = float(input())
        MnaKM(M)
        print(M, 'mili w przeliczeniu na kilometry to: ', MnaKM(M))
    elif wybor == 'KMnaM':
        print('Wpisz odleglosc: ')
        KM = float(input())
        KMnaM(KM)
        print(KM, 'kilometrow w przeliczeniu na mile to: ', KMnaM(KM))
    else:
        print("Bledny wybor")

    print("Czy wykonac ponownie t/n")
    decyzja = input()