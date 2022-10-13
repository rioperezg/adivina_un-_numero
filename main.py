import random
numero = random,random.randint(0, 100)
print ("introduzca un numero a adivinaffffffr")
while True:
    numero = input("introduzca un numero entre 0 y 99")

    try:
        numero = int(numero)
    except:
        pass
    else:
        if 0 <= numero <= 99:

           break
