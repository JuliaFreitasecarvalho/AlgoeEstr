nomeproduto= input("Insira o nome do produto")
quantidade= int(input("Quantidade"))
precouni= float(input("Insira preço unitário"))

preco= quantidade*precouni
if preco> 100:
    desconto= preco*0.95
    print(f"Total cm 5% de desconto {desconto}")
else:
    print(f"Total R${preco}")
