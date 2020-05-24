#turnos=input('Ingrese el numero de turnos:')
palabra=input('Ingrese la palabra a adivinar:')
while len(palabra)<5:
    print('Hey, palabra minimo de 5 letras pelagato!')
    palabra=input('Ingrese la palabra a adivinar:')
intento=5
acumu=""

while(intento>0):

    adiv = input("\nIngrese letra o palabra:") 
    acumu = acumu + adiv

    if adiv in palabra:
        acierto = True
        for letra in palabra:      
            if letra in acumu:    
                print(letra,end=' '),   
            else:
                print ('.',end=' ') 
                acierto = False
        if acierto:
            print("\n Ganaste")
            break
    elif adiv==palabra:
        print("\n Ganaste")
        break
    else:
        for letra in palabra:      
            if letra in acumu:    
                print(letra,end=' '),   
            else:
                print ('.',end=' ') 
        intento=intento-1
        print(f'\nLetra no encontrada, te quedan {intento} intentos')
        if intento == 0:
            print('Perdiste')

