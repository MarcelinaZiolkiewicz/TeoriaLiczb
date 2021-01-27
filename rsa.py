import random

def euclid(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi
    
    while e > 0:
        temp1 = temp_phi//e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2
        
        x = x2- temp1* x1
        y = d - temp1 * y1
        
        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d + phi

def encrypt(d,n, message):  
    print("   Szyfrowanie...")
    encryptedMsg = [(ord(char) ** d) % n for char in message]
    return encryptedMsg

def decrypt(e,n, decryptedMsg):
    print("   Deszyfrowanie...")
    decryptedText = [chr((char ** e) % n) for char in decryptedMsg]
    return ''.join(decryptedText)
    
def checkPrime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True

def generatePrime():
    isPrime = True
    
    while isPrime:
        #Zakres ograniczyłem do 1000 ze względu na długi czas szyfrowania i deszyfrowania wiadomości 
        possiblePrime = random.randrange(10, 1000)
        
        if checkPrime(possiblePrime):
            isPrime = False

    print("-> Znaleziono liczbe pierwsza: ", possiblePrime)
    return possiblePrime


def inputValue():
    inptOk = True

    while inptOk:
        p = int(input("Podaj liczbę pierwszą np.: 107, 1619, 23, 97  "))
        q = int(input("Podaj drugą liczbę pierwszą inną niż wcześniej: "))
        
        if (checkPrime(p) and checkPrime(q)):
            print("Wartości poprawne")
            inptOk = False
        elif p == q:
            print("Wartości 'p' i 'q' nie mogą być takie same")

        else:
            print("Obie wartości muszą być liczbami pierwszymi")

    return (p,q)

def manualOrAuto():
    p = 0
    q = 0

    while True:
        val = input("[1] Podaj 'p' i 'q' ręcznie \n[2] Wygeneruj 'p' i 'q' losowo\n")

        if val == "1":
            p,q = inputValue()
            break
        elif val == "2":
            p = generatePrime()
            q = generatePrime()
            break
        else:
            print("-> Wybierz opcję [1] lub [2]\n")

    return p,q

def rsaSteps():
    

    print("\n -- Szfrowanie i deszyfrowanmie wiadomości za pomocą rsa -- \n")

    print("Na samym początku musimy wygenerować klucze")
    print("Dlatego wybieramy p i q na podstawie których będziemy przeprowadzać dalsze obliczenia: ") 
    
    p,q = manualOrAuto()
    
    print("Wyliczamy p i q ze wzoru -> n = ", p, "*", q)
    n = p * q
    print("-> ", n)
    print("Teraz wyliczamy funkcję Eulera: ")
    phi = (p-1) * (q-1)
    print("-> ", phi)
    print("Losowo wybieramy liczbę e która musi spełniać warunek 1 < e < phi i sprawdzamy czy jest względnie pierwsza")
    e = random.randrange(1, phi)

    #sprawdzanie czy liczba jest wzglęnie pierwsza algorytmem euklidesa
    g = euclid(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = euclid(e, phi)

    print("-> ", e)

    d = inverse(e, phi)
    print("Po tych wszystkich działaniach mamy nasze klucze tj: ")
    print("   -> Prywatny: ", d, n)
    print("   -> Publiczny: ", e, n)

    msg = input("Wprowadz wiadomość do zaszyfrowania: ")
    encrypted = encrypt(d,n,msg)
    print(" -> ", encrypted)
    print("Odszyfrowana: ", decrypt(e,n,encrypted), '\n')
