import random
max = int(input("Ingresa el número máximo a adivinar: "))
numero = random.randrange(max)
adivina = int(input("¿qué número eligió el computador?:"))
if (adivina == numero):
    print("Felicitaciones")
else:
    if adivina > numero:
        print("El número era menor que", adivina)
    else:
        print("El número era mayor que", adivina)
print("El número era", numero)