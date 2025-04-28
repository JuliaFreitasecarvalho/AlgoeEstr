ba= int(input("Insira número base: \n"))
ini= int(input("Insira número para começar: \n"))
fi= int(input("Insira número para acabar: \n"))

def tabuada_personalizada(base, inicio, fim):
    print(f"tabuada do {base} de {inicio} a {fim}")
    for i in range (inicio, fim+1):
        print(f"{base} x {i} = {base*i}")

tabuada_personalizada(ba, ini, fi)
