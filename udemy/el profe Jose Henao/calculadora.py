"""
Crear una calculadora que realice las 4 operaciones
básicas (suma, resta, multiplicación y división). Se debe mostrar un
menú con las cuatro opciones indicadas. El usuario debe ingresar la
opción que desee; de acuerdo a la opción seleccionada se deben
pedir los datos correspondientes y mostrar el resultado correcto.
Debe existir la opción de que el usuario pueda salir del programa.
Cada vez que el programa finalice una operación se debe mostrar de
nuevo el menú de opciones
"""

a = int(input('Primer valor de la operacion'))
b = int(input('Primer valor de la operacion'))
oper = input('Ingrese la operacion que desea realizar, solo ingrese la primera letra, Suma (S), Resta (R), Multiplicacion (M), Division(D)')

if oper == 'S':
    sum = a+b
    print(sum)
elif oper == 'R':
    sum = a-b
    print(sum)
elif oper == 'M':
    sum = a*b
    print(sum)
elif oper == 'D':
    sum = a/b
    print(sum)

    
