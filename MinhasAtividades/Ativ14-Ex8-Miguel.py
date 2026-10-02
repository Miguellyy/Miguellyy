uv = int(input("Qual o indice UV? "))

if uv < 3:
    print("Baixo, não precisa de proteção.")
elif uv <= 5:
    print("Moderado, use protetor FPS 30")
elif uv <= 7:
    print("Alto, use protetor FPS 50 e óculos.")
elif uv <= 10:
    print("Muito alto, evite exposição entre 10h e 16h.")
elif uv >= 11:
    print("Extremo, não saia ao sol!")
    

    
    
    
    
