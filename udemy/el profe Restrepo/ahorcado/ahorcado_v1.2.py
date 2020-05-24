#turnos=input('Ingrese el numero de turnos:')
palabra = input('Ingrese la palabra a adivinar:')
while len(palabra) < 5:
    print('Hey, palabra minimo de 5 letras pelagato!')
    palabra = input('Ingrese la palabra a adivinar:')
intento = 5
acumu = ""


def imprima_palabra():
    acierto = True
    for letra in palabra:
        if letra in acumu:
            print(letra, end=' '),
        else:
            print('.', end=' ')
            acierto = False
    return acierto


while(intento > 0):

    adiv = input("\nIngrese letra o palabra:")
    if adiv in acumu:
        print('Ya mencionaste esa letra!')
    else:
        acumu = acumu + adiv
        if adiv in palabra:
            result = imprima_palabra()
            if result:
                print("\nAcertaste a todas las letras, muy bien!")
                break
            elif adiv == palabra:
                print("\nAdivinaste la palabra completa!")
                break
        else:
            imprima_palabra()
            intento -= 1
            print(f'\nLetra no encontrada, te quedan {intento} intentos')
            if intento == 0:
                print('Perdiste')
