# #tabuada do 7
# print("Tabuada do 7:")
# for i in range(1,11):
#     print("7 x", i, "=", 7*i)

# #tabuada do 8
# print("Tabuada do 7:")
# for i in range(1,11):
#     print("8 x", i, "=", 8*i)

# #tabuada do 9
# print("Tabuada do 7:")
# for i in range(1,11):
#     print("9 x", i, "=", 9*i)



# #Código em python para exibir as tabuadas de 7,8,9
# def tabuada(numero): #Def começa uma função
#     print(f"Tabuada do {numero}")
#     for i in range(1,11):
#         print(f"{numero} x {i} = {numero * i}")
# #exibindo as tabuadas
# # tabuada(7)
# # tabuada(8)
# # tabuada(9)

# for i in range(1,101):
#     tabuada(i)


#tabuada personalizda em Python
def tabuada_personalizada(base, inicio, fim):
    print(f"tabuada do {base} de {inicio} a {fim}")
    for i in range (inicio, fim+1):
        print(f"{base} x {i} = {base*i}")

tabuada_personalizada(7,1,10)
tabuada_personalizada(5,5,15)