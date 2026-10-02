senha = str(input("Qual sua senha?: "))

if len(senha) >= 8:
    print("Senha forte, bem segura")
else:
    print("Senha fraca, use mais de 8 caracteres.")