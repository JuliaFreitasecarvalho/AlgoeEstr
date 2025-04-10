idade= int(input("Insira idade"))
membro= input("É membro do nosso clube?")
acompanhante= input("Está sendo acompanhado por um membro?")

if idade>=18:
   print("Maior de idade, pode proceguir.")
else:
   print("Menor de idade, proibido de entrar no clube.") 

if membro == "não":
    print("Deverá pagar um ingresso")
else:
   print("Entrada gratuita")

if acompanhante == "sim":
    print("Pagará meia entrada")
else:
   print("Pagará inteira")