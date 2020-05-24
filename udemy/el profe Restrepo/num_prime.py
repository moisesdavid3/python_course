# Primos

# ## Encuentre numeros primos de la lista
# lista = [1,4,5,7,9,12,15,16,20,21,26]
# primos=[]
# for num in lista:
#     if all(num%i!=0 for i in range(2,num)):
#        primos.append(num)
# primos.reverse()
# print(primos)


# ## Ingrese los valores y luego encuentre los nums primos
# item=input("How many numbers do you want?: ")
# lista=[]
# primos=[]

# while len(lista)<int(item):
#     b=input("Enter the numbers of the list")
#     lista.append(b)
# lista1=map(int,lista)

# for num in lista1:
#     if all(num%i!=0 for i in range(2,num)):
#         primos.append(num)
# primos.sort(reverse=True)
# print(primos)


# ## Funcion para saber si un num es primo o no
# def is_primo(num):
#     if all(num%i!=0 for i in range(2,num)):
#         print('True')
#     else:
#         print('False')
# is_primo(9)

