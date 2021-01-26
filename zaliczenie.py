import rsa

#Python 3.8.3

def menu():
    while 1:
        print("-- MENU --")
        print("1) Liczby pierwsze z przedziału: 1'999'900'000 - 2'000'099'990")
        print("2) Test Fermata") 
        print("3) Czynniki pierwsze podanej liczby")
        print("4) Funkcja Eulera dla liczby")
        print("5) Algorytm Euklidesa")
        print("6) Szfrowanie RSA")
        print("7) Wyjście")

        wyb = int(input("Chose option: "))

        if wyb == 1:
            print("-> Liczby pierwsze w przedziale to: ")
        
        elif wyb == 2:
            print("-> Test Fermata")

        elif wyb == 3:
            print("-> Czynniki pierwsze")
            
        elif wyb == 4:
            print("-> Funkcja Eulera")

        elif wyb == 5:
            print("-> Algorytm Euklidesa")

        elif wyb == 6:
            print("-> Szyfrowanie RSA")
            rsa.rsaSteps()

        elif wyb == 7:
            print("Dziękujemy za skorzystanie z programu")
            break

        else:
            print('Incorrect value')


menu()