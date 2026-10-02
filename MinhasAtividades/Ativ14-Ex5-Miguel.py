kwh = float(input("Quantos kWh você consome por mês?: "))

if kwh <= 100:
    kwh = kwh * 0.40
    print(f"O valor total que você deverá pagar é R${kwh}")
elif kwh <= 300:
    kwh = kwh * 0.65
    print(f"O valor total que você deverá pagar é R${kwh}")
else:
    print(f"O valor total que você deverá pagar é R${kwh}")


    
    
    
    
