while True:
    choice = 0
    num1 = 0
    num2 = 0
    result = 0
    print("1 - Somar dois números")
    print("2 - Multiplicar dois número")
    print("3 - Sair\n")
    choice = int(input("Escolha!!!: "))

    if choice == 1:
        print("Você escolheu somar!!!!")
        num1 = int(input("Escolha o primeiro número: "))
        num2 = int(input("Escolha o segundo número: "))
        result = num1 + num2
        print(f"{num1}+{num2}={result}")
    if choice == 2:
            print("Você escolheu multiplicar!!!!")
            num1 = int(input("Escolha o primeiro número: "))
            num2 = int(input("Escolha o segundo número: "))
            result = num1 * num2
            print(f"{num1}x{num2}={result}")
    if choice == 3:
        break