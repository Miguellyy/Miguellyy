ganhohora = float(input("Quanto você ganha por hora?: "))
horatrab = int(input("Quantas horas você trabalha por mês?: "))
bruto = ganhohora * horatrab

ir = bruto * 0.11
inss = bruto * 0.08
sindicato = bruto * 0.05
desconto = ir + inss + sindicato

print("=========================SALÁRIO MENSAL============================\n")

print(f"+ Salário bruto: R${bruto}\n")
print(f"- IR (11%): R${ir}\n")
print(f"- INSS (8%): R${inss}\n")
print(f"- Sindicato (5%): R${sindicato}\n")

print("=========================VOCÊ IRÁ RECEBER============================\n")

print(f"= Salário Liquido: R${bruto - desconto}\n")

print("=====================================================================\n")
