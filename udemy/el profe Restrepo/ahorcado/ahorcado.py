turnos = input('Ingrese el numero de turnos:')
palabra = input('Ingrese la palabra a Adivinar:')
intento = int(turnos)
acumu = ''

while(intento > 0):
    fallo = 0
    adiv = input("\nIngrese letra:")
    acumu = acumu + adiv
    if adiv not in palabra:
        intento -= 1
        print("Fallo")
        if intento == 0:
            print("Pierdes")

    for letra in palabra:
        if letra in acumu:
            print(letra, end=' '),
        else:
            print('.', end=' '),
            fallo += 1
    if fallo == 0:
        print("\nAdivinaste")
        break
