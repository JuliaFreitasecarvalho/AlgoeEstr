notas=[]
for i in range (1,6):
    nota= int(input("Insira nota do aluno"))
    notas.append(nota)
soma= 0
for nota in notas:
    soma= soma+ nota

media= soma/5
print(f"{media}")