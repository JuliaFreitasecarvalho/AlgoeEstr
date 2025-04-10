print("Bem vindo ao programa mais preconceituoso existente")
idade= int(input("Insira idade"))
genero= input("Insira gênero")
atleta= input("É atleta")

if genero == "feminino" or genero == "masculino":
    print("Gênero existente")
else:
    print("Gênero não existente, insira entre feminino e masculino")

if idade<15:
    print("Oferecer artigos infantis")
elif idade>= 15 and idade<21 and genero == "feminino":
    print("Oferecer maquiagem moda")
elif idade>= 15 and idade<32 and genero == "masculino":
    print("Oferecer artigos de esporte")
elif idade>=15 and idade<=21 and genero == "masculino" and atleta == "não":
    print("Oferecer videogames")
elif idade>=21 and idade<=32 and genero == "masculino" and atleta == "não":
    print("Oferecer livros, jardinagem e eletrodomesticos")
elif idade>=22 and idade<=35 and genero == "feminino":
    print("Oferecer artigos esportivos e itens de casa")