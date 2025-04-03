print("Bem vindo ao programa mais preconceituoso existente")
idade= int(input("Insira idade"))
genero= input("Insira gênero")

if genero == "Feminino" or genero == "Masculino":
    print("Gênero existente")
else:
    print("Gênero não existente, insira entre feminino e masculino")

if idade<15:
    print("Oferecer artigos infantis")
elif idade>= 15 and idade<21 and genero == "Feminino":
    print("Oferecer maquiagem moda")
elif idade>= 15 and idade<32 and genero == "Masculino":
    print("Oferecer artigos de esporte")