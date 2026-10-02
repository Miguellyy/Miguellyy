idade = int(input("Qual a sua idade?: "))

if idade < 12:
    print("Categoria Infantil")
elif idade <= 17:
    print("Categoria Juvenil")
else:
    print("Categoria Adulto")