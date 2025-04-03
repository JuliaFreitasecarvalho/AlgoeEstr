nota1= float(input("Insira primeira nota"))
nota2= float(input("Insira segunda nota"))
nota3= float(input("Insira terceira nota"))

media= (nota1+nota2+nota3)/3
print(f"Media igual a {media}")

if media>= 7:
    print("Aprovado")
elif media ==6 or media<7:
    print("Recuperação")
else:
    print("Reprovado")