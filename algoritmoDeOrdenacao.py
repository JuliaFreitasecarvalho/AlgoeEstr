# lista = [1,3,5,7,8,0,2,4,6,8]

# #lista_ordenada = sorted(lista)
# #print(lista_ordenada)

# def bubbleSort(lista): 
#     for passrnum in range(len(lista)-1,0,-1):
#         for i in range(passrnum): 
#             if lista[i] > lista[i+1]:
#                 temp = lista[i] 
#                 lista[i] = lista[i+1]
#                 lista[i+1] = temp
    
# bubbleSort(lista)
# print(lista)

lista = [3,7,5,2,1]
def selection_sort (lista):
    n = len(lista)
    for i in range (n -1, 0, -1):
        indice_maior = 0
        for j in range (1, i+1):
            if lista[j] > lista[indice_maior]:
                indice_maior = j
        lista[i], lista[indice_maior] = lista[indice_maior], lista[i]
        print(f"Lista após a intereção{(i-n)*-1}",lista)

    