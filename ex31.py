num = int(input("Insira numero: \n"))
def tabuada(numero): #Def começa uma função
    print(f"Tabuada do {numero}")
    for i in range(1,11):
        print(f"{numero} x {i} = {numero * i}")

tabuada(num)