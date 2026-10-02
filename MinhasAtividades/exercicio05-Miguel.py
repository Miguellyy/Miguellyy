num = int(input("Digite um numero (0 para sair): "))
soma = 0
while num != 0:
    soma = soma + num
    num = int(input("digite um numero (0 para sair): "))
print(f"a soma é : {soma}")