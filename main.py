import random

repetir = 1
cont_t = 0

while repetir == 1:

    codigo = random.randint(1000, 9999)

    print("""\n
    ==> Bem vindo ao NumGuess!!! <==

    Você tem 10 tentativas para acertar um numero entre 1000 e 9999, 
    a partir da 5° tentativa o jogo começara a te ajudar com dicas.
        Boa sorte!
    """)

    input("<<<Pressione enter>>>") 

    num_tentativas = 0
    tentativas_restantes = 10 

    while num_tentativas < 10:
        tentativa = int(input("\nDigite seu palpite: "))

        if tentativa < 1000 or tentativa > 9999:
            print("")
            print(" --------------------------------------- ")
            print("\n>>> ATENÇÃO!!! <<<\nO numero deve ser entre >>>1000 e 9999<<<")
            num_tentativas -= 1
            tentativas_restantes += 1
        else:
            num_tentativas += 1
            tentativas_restantes -= 1

            if tentativa == codigo:
                print(" --------------------------------------- ")
                print(" ")
                print(f"""P A R A B E N S!\nvocê acertou!\nVocê precisou de {num_tentativas} tentativas!\nO código era: {codigo}""")
                print(" ")
                print(" --------------------------------------- ")
                repetir = int(input("Você deseja reiniciar o jogo? (Digite 1 para SIM e 0 para NÃO): "))
                break
    
            codigo_1 = codigo // 1000
            codigo_2 = (codigo % 1000) // 100
            codigo_3 = (codigo % 100) // 10
            codigo_4 = codigo % 10
    
            tentativa_1 = tentativa // 1000
            tentativa_2 = (tentativa % 1000) // 100
            tentativa_3 = (tentativa % 100) // 10
            tentativa_4 = tentativa % 10
    
            print("\n\n --------------------------------------- ")
            print(f"\nSua tentativa nesta rodada foi: {tentativa}\n")
            print("Acertos: ", end="")
    
            if codigo_1 == tentativa_1:
                print(codigo_1, end="")
                cont_t += 1
            else:
                print("_", end="")
    
            print(" ", end="")
    
            if codigo_2 == tentativa_2:
                print(codigo_2, end="")
                cont_t += 1
            else:
                print("_", end="")
    
            print(" ", end="")
    
            if codigo_3 == tentativa_3:
                print(codigo_3, end="")
                cont_t += 1
            else:
                print("_", end="")
    
            print(" ", end="")
    
            if codigo_4 == tentativa_4:
                print(codigo_4)
                cont_t += 1
            else:
                print("_")
    
            print(f"\nVocê acertou > {cont_t} < digitos nesta tentativa.")
            print(f"Você ERROU! Você ainda tem >>> {tentativas_restantes} <<< tentativas restantes")
            cont_t -= cont_t
    
            if num_tentativas >= 5 and num_tentativas < 10:
                print("\nDica: ", end="")
                dica_valida = 0
    
                while dica_valida == 0:
                    slot_dica = random.randint(1, 4)
                    rand_dica = random.randint(1, 2)
    
                    if slot_dica == 1:
                        if codigo_1 != tentativa_1:
                            dica_valida = 1
                            if rand_dica == 1:
                                if codigo_1 % 2 == 0:
                                    print("O primeiro dígito é > PAR <")
                                else:
                                    print("O primeiro dígito é > ÍMPAR <")
                            else:
                                if codigo_1 > tentativa_1:
                                    print(f"O primeiro dígito é maior que {tentativa_1}")
                                else:
                                    print(f"O primeiro dígito é menor que {tentativa_1}")
    
                    if slot_dica == 2:
                        if codigo_2 != tentativa_2:
                            dica_valida = 1
                            if rand_dica == 1:
                                if codigo_2 % 2 == 0:
                                    print("O segundo dígito é > PAR <")
                                else:
                                    print("O segundo dígito é > ÍMPAR <")
                            else:
                                if codigo_2 > tentativa_2:
                                    print(f"O segundo dígito é maior que {tentativa_2}")
                                else:
                                    print(f"O segundo dígito é menor que {tentativa_2}")
    
                    if slot_dica == 3:
                        if codigo_3 != tentativa_3:
                            dica_valida = 1
                            if rand_dica == 1:
                                if codigo_3 % 2 == 0:
                                    print("O terceiro dígito é > PAR <")
                                else:
                                    print("O terceiro dígito é > ÍMPAR <")
                            else:
                                if codigo_3 > tentativa_3:
                                    print(f"O terceiro dígito é maior que {tentativa_3}")
                                else:
                                    print(f"O terceiro dígito é menor que {tentativa_3}")
    
                    if slot_dica == 4:
                        if codigo_4 != tentativa_4:
                            dica_valida = 1
                            if rand_dica == 1:
                                if codigo_4 % 2 == 0:
                                    print("O quarto dígito é > PAR <")
                                else:
                                    print("O quarto dígito é > ÍMPAR <")
                            else:
                                if codigo_4 > tentativa_4:
                                    print(f"O quarto dígito é maior que {tentativa_4}")
                                else:
                                    print(f"O quarto dígito é menor que {tentativa_4}")
    else:
            print(" --------------------------------------- ")
            print("\nD E R R O T A!")
            print("Uma pena você perdeu!")
            print(f"O numero de tentativas >>> ACABARAM! <<<\nO codigo correto era >>> {codigo} <<<")
            print(f"Sua ultima tentativa foi: {tentativa}\n")
            print(" --------------------------------------- ")
            repetir = int(input("Você deseja reiniciar o jogo? (Digite 1 para SIM e 0 para NÃO): \n\n"))

    if repetir != 1 and repetir != 0:
        while repetir != 1 and repetir != 0:
            print("""\nResponda >> APENAS << com >> 1 ou 0 << 
(1 para SIM e 0 para NÃO)""")

            repetir = int(input("Você deseja reiniciar o jogo? (Digite 1 para SIM e 0 para NÃO): "))
