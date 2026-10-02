import random
import os
import time

os.system('cls')

print("Bem vindo ao CASSINO do GRIFO!")
input("Pressione enter para JOGAR...")
time.sleep(2)
print("Vamos lhe dar R$500 para brincar, só não perca tudo")
input("Pressione enter para continuar...")

money = 500

while money > 0:
    rng = random.randint(0, 36)

    time.sleep(1)
    os.system('cls')

    print(f"SALDO: R${money}")
    aposta = 0
    while True:
        try:
            while True:
                aposta = float(input("Quantos reais você deseja apostar??: "))
                while aposta <= 0 or aposta > money:
                    print("Não é permitido apostar nada ou apostar mais do que tem.")
                    break
                break
        except ValueError:
            print("Letras não são permitidas.")
        if aposta > 0 and aposta <= money:
            break

    money = money - aposta
    escolha = ""
    os.system('cls')

    # ESCOLHAS

    print("Iremos rodar uma roleta com números de 0 a 36, advinhe o que será o número que vai cair, ou qual será...")
    print("-----------------------------------------------------------------------------------------------------")
    time.sleep(.2)
    print("1 - Número Par (2x)")
    time.sleep(.2)
    print("2 - Número Impar (2x)")
    time.sleep(.2)
    print("3 - Número Especifico (0 - 36) (10x)")
    time.sleep(.2)
    print(f"SALDO: R${money}")
    time.sleep(.2)
    print(f"APOSTANDO: R${aposta}")
    print("-----------------------------------------------------------------------------------------------------")

    time.sleep(.3)
    escolha = str(input("Aonde você deseja por a sua sorte? (digite número): "))

    match escolha:
# CASO DO PAR
        case '1':
            if rng % 2 == 0:
                os.system('cls')
                time.sleep(2)
                print(f"A roleta caiu em... {rng}!")
                time.sleep(.7)
                print("Parabéns, você acertou, o número é Par!")
                money = money + (aposta * 2)
                time.sleep(.7)
                print(f"Seu saldo é: R${money}")
                input("Pressione enter para continuar...")
            else:
                os.system('cls')
                time.sleep(2)
                print(f"A roleta caiu em... {rng}!")
                time.sleep(.7)
                print("Infelizmente você perdeu, o número é Impar.")
                time.sleep(.7)
                print(f"Seu saldo é: R${money}")
                time.sleep(2)
                input("Pressione enter para continuar...")
# CASO DO IMPAR
        case '2':
            if rng % 2 != 0:
                os.system('cls')
                time.sleep(2)
                print(f"A roleta caiu em... {rng}!")
                time.sleep(.7)
                print("Parabéns, você acertou, o número é Impar!")
                money = money + (aposta * 2)
                time.sleep(.7)
                print(f"Seu saldo é: R${money}")
                input("Pressione enter para continuar...")
            else:
                os.system('cls')
                time.sleep(2)
                print(f"A roleta caiu em... {rng}!")
                time.sleep(.7)
                print("Infelizmente, você perdeu, o número é par.")
                time.sleep(.7)
                print(f"Seu saldo é: R${money}")
                time.sleep(2)
                input("Pressione enter para continuar...")
# CASO DA ESCOLHA DE NUMERO
        case '3':
            os.system('cls')
            numchoice = -1
            while True:
                try:
                    while True:
                        numchoice = int(input("Por favor insira um número de 0 a 36: "))
                        while numchoice < 0 or numchoice > 36:
                            print("Apenas números de 0 a 36 são permitidos.")
                            break
                        break
                except ValueError:
                    print("Letras não são permitidas.")
                if numchoice >= 0 and numchoice <= 36:
                    break

            if numchoice == rng:
                os.system('cls')
                print("Meus parabéns, você deu a sorte grande.")
                time.sleep(.5)
                money = money + (aposta * 10)
                print(f"O número que você escolheu foi: {numchoice}")
                time.sleep(.5)
                print("O número que caiu foi exatamente o mesmo.")
                time.sleep(.7)
                print(f"Seu saldo agora é: R${money}")
                input("Pressione enter para continuar...")
            else:
                os.system('cls')
                time.sleep(1)
                print(f"Você escolheu {numchoice}")
                time.sleep(.3)
                print(f"Número que caiu: {rng}")
                time.sleep(1)
                print("Não foi dessa vez.")
                time.sleep(.7)
                print(f"Seu saldo: R${money}")
                input("Pressione enter para continuar...")
        case _:
            print("Escolha uma opção válida")
            money = money + aposta
            input("Pressione enter para voltar a tela de aposta...")
os.system('cls')
time.sleep(2)
print("Meu parabéns!!")
time.sleep(.7)
print("Você perdeu todo o seu dinheiro!")
time.sleep(.7)
print("Não caia no vicio dos jogos de azar.")
time.sleep(.7)
print("Vem pro MI!")