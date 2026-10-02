pedestres = str(input("Tem pedestres? [sim/não]: ")).lower()

if pedestres == "sim":
    pedestresBool = True
else:
    pedestresBool = False

semaforo = str(input("Que cor está o semáforo?: "))

if semaforo.lower() == "verde" and pedestresBool == False:
    print("Pode seguir em frente")
elif semaforo.lower() == "verde" and pedestresBool == True:
    print("Atenção! Pedestres na faixa, reduza velocidade!")
elif semaforo.lower() == "amarelo":
    print("Prepare-se para parar!")
elif semaforo.lower() == "vermelho":
    print("Pare e aguarde o sinal abrir!")
else:
    print("O sinal está com defeito, prosiga com cautela.") 