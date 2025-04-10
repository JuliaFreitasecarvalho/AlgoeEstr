palavras=[]
i= 0
for i in range(1,7):
    palavra= input("Insira palavra")
    palavras.append(palavra)

for palavra in palavras:
    print(len(palavra))

    if len(palavra)>5:
        i=i+1
    print(f"A quantidade de de palavras com 5 caracteres é:{i}")
    print(palavras)