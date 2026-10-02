conta = float(input("Informe o valor de sua conta: "))
aval = str(input("Avalie nosso serviço: "))
inpt = aval.lower()

if inpt == "bom":
    conta = conta + (conta*0.10)
    print("Você disse que nosso serviço é bom.")
    print("Por isso você recebe 10% de gorjeta.")
    print(f"Seu total será {conta}")
elif inpt == "ótimo":
    conta = conta + (conta*0.15)
    print("Você disse que nosso serviço é ótimo!.")
    print("Por isso você recebe 15% de gorjeta.")
    print(f"Seu total será {conta}")
else:
    print(f"Você disse que nosso serviço é {aval}")
    print("Você não receberá gorjeta.")
    print(f"Seu total será {conta}")
    
    
    
