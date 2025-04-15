valores=[]
novosv=[]
for i in range(1,5):
    valor=int(input("insira o valor"))
    valores.append(valor)

adicional=int(input("insira um numero para multiplica-los "))
for valor in valores:
    novosv.append(valor*adicional)
print(f"O resultado é {novosv}")