num = int(input("Digite um numero inteiro: "))
contagem = 0

for i in range(2, (num//2 + 1)):
    if(num % i == 0):
        contagem = contagem + 1
        break
if contagem == 0 and num != 1:
    print(f"É primo")
else:
    print("NÉ PRIMO NAO")
