numeros=[]
for i in range (0,4):
    numero=int(input("insira valor inteiro"))
    numeros.append(numero)

maior= numeros[0]
for numero in numeros:
    if numero> maior:
        maior= numero
    
print(f"{maior} é maior")

menor= numeros[0]
for numero in numeros:
    if numero<menor:
        menor= numero
     
print(f"{menor} é menor")