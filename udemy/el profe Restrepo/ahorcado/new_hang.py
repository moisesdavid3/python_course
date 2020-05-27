# word1 = 'hola'
# word2 = ''

# for i in word1:
#     word2 += i
#     if word1 == word2:
#         print('iguales')
#     else:
#         print('no son iguales')
intento = 5
completas = []
while(intento > 0):
    completa = ""
    adiv = input("\nIngrese letra o palabra:")
    if len(adiv) > 1:
        completa += adiv
        intento -= 1

    if completa in completas:
        print('Ya esta dentro')
    else:
        completas.append(completa)


print(completas)
