lista = [25,1,12,15,8,16,21,4,20,7,9]
pares = []

for num in lista:
    if num % 2 == 0:
        pares.append(num)
print(pares)

pares = [i for i in lista if i%2==0]
print(pares)


# Ordenar una lista sin usar sort()

# for i in range(len(lista)):
#     for j in range(i + 1, len(lista)):
#         if lista[i] > lista[j]: # > = ascendente < = descendente
#            lista[i], lista[j] = lista[j], lista[i]
# print (lista)