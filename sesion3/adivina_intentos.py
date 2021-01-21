import random
max = int(input("Ingresa el número máximo a adivinar: "))
numero = random.randrange(max)
intento = 1
while intento <= 3:
    print("Intento #", intento)
    adivina = int(input("¿qué número eligió el computador?: "))
    if (adivina == numero):
        print("Felicitaciones")
        break
    else:
        if adivina > numero:
            print("Estás cerca. El número es menor que", adivina)
        else:
            print("Estás cerca. El número es mayor que", adivina)
    intento = intento + 1

if intento > 3:
    print("Más suerte para la próxima. El número era", numero)