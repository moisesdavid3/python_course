"""
- Ejercicio 2: Crear un algoritmo para calcular el precio final de una
compra dado el precio de la compra; las condiciones son:
- Si la compra es menor a $100.000 no hay descuento
- Si el precio de la compra está entre $ 100.000 y $249.999 hay
un descuento del 20% sobre el precio total
- Si el precio está entre $250.000 y $499.999 se aplica un
descuento del 25% sobre el precio total
- Finalmente si la compra tiene un valor de $500.000 o más se
aplica un descuento del 30% sobre el precio total

- Modifique el ejercicio anterior de modo que se valide que la entrada
sea un valor numérico mayor a 0 y muestre un mensaje de error en
caso de que el precio ingresado de la compra sea negativo.
"""

price = input('Ingrese el precio de la compra')
#precio = int(price)

while(price <= 0):
    print('Error')
    price = input('Ingrese el precio de la compra')
    precio = int(price)


if(0 < precio < 100000):
    print(f'El precio de su compra es {precio}')
elif(100000 < precio < 249999):
    new_precio = precio*0.8
    print(f'El precio de su compra es {new_precio}')
elif(250000 < precio < 499999):
    new_precio = precio*0.75
    print(f'El precio de su compra es {new_precio}')
else:
    new_precio = precio*0.7
    print(f'El precio de su compra es {new_precio}')
