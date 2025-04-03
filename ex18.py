salariobase= float(input("Insira salário base"))
horas= float(input("Insira horas extras trabalhadas"))
valorextra= float(input("Valor pago por horas extras"))

total= (valorextra*horas)+ salariobase
print(f"O valor total é {total}")
