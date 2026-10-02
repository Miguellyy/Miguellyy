dispo = str(input("Há quartos disponiveis? (sim ou não): "))
diaria = 250

if dispo.lower() == "não":
    print("Desculpa, não há quartos disponiveis.")
elif dispo.lower() == "sim":
    socio = str(input("O hóspede é sócio do clube de fidelidade? (sim ou não): "))
    noites = int(input("Quantas noites serão? "))
    if socio.lower() == "sim":
        print("Você terá desconto de 20% sobre a diária de R$250,0")
        diaria = diaria - (diaria*0.20)
        diaria = diaria * noites
        print(f"O valor final que o hóspede irá pagar será: {diaria}")
    elif socio.lower() == "não":
        print("A diária será R$250,0")
        diaria = diaria * noites
        print(f"O valor final que o hóspede irá pagar será: {diaria}")
    

    