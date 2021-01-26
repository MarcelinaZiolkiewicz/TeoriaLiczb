import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def multiplicative_inverse(e, phi):
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

def encrypt(d,n, plaintext):

    #Convert each letter in the plaintext to numbers based on the character using a^b mod m
    cipher = [(ord(char) ** d) % n for char in plaintext]
    #Return the array of bytes
    return cipher

def decrypt(e,n, ciphertext):

    #Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = [chr((char ** e) % n) for char in ciphertext]
    #Return the array of bytes as a string
    return ''.join(plain)
    

def rsaSteps():
    print("Szfrowanie i deszyfrowanmie wiadomości za pomocą rsa\n")

    print("Na samym początku musimy wygenerować klucze")
    print("Dlatego wybieramy p i q na podstawie których będziemy przeprowadzać dalsze obliczenia: ") 
    # dodać opcje z automatycznym wyborem p i q
    p = int(input("Podaj liczbę pierwszą np.: 1619, 23, 97  "))
    q = int(input("Podaj drugą liczbę pierwszą inną niż wcześniej: "))
    
    print("Wyliczamy p i q ze wzoru -> n = ", p, "*", q)
    n = p * q
    print(n)
    print("Teraz wyliczamy funkcję Eulera: ")
    phi = (p-1) * (q-1)
    print(phi)
    print("Losowo wybieramy liczbę e która musi spełniać warunek 1 < e < phi i sprawdzamy czy jest względnie pierwsza")
    e = random.randrange(1, phi)

    #sprawdzanie czy liczba jest wzglęnie pierwsza algorytmem euklidesa
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    print("Liczba e: ", e)

    d = multiplicative_inverse(e, phi)
    print("Po tych wszystkich działaniach mamy nasze klucze tj: ")
    print("Prywatny: ", d, n)
    print("Publiczny: ", e, n)

    msg = input("Wprowadz wiadomość do zaszyfrowania: ")
    encrypted = encrypt(d,n,msg)
    print(encrypted)
    print("Odszyfrowana: ", decrypt(e,n,encrypted))

rsaSteps()
#trzeba dodać walidację do wprowadzania liczb i dodawanie losowe p,q