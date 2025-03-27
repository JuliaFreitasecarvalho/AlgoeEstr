login= input("Insira email")
senha= input("Insira senha")

email= str.lower(login)
if len (senha) >=8:
    print("Login efetuado com sucesso")
else:
    print("Login ou senha errados")