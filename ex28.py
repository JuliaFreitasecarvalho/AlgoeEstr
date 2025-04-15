numeros=[]
pares=[]
impares=[]
for i in range(0,8):
    numero=int(input(f"insira o valor"))
    numeros.append(numero)

for numero in numeros:
    m=numero % 2
    if m==0:
        par=numero
        pares.append(par)
    else:
        impar=numero
        impares.append(impar)

print(f"{pares} são pares e {impares} são impares")
