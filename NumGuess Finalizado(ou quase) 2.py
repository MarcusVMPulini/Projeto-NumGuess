import random

repetir = 1
cont_t = 0

#loop para reiniciar o jogo

while repetir == 1:
    
    codigo = random.randint(1000, 9999) #gera o codigo aleatorio

    print("""
    ==> Bem vindo ao NumGuess!!! <==

    Você tem 10 tentativas para acertar um numero entre 1000 e 9999, 
    a partir da 5° tentativa o jogo começara a te ajudar com dicas.
        Boa sorte!
    """)

    TecleAlgo = input("<<<Pressione enter>>>") 

    print(" ")

#variaveis para contabilizar o numero de tentativas e de tentativas restantes

    num_tentativas = 0
    tentativas_restantes = 10 

#loop para receber as tentativas

    while num_tentativas < 10:
        print(" ")
        tentativa = int(input("Digite seu palpite: "))

        num_tentativas += 1
        tentativas_restantes -= 1

        if tentativa == codigo:
            print(" --------------------------------------- ")
            print(" ")
            print(f"""Sua tentativa nesta rodada foi: {tentativa}
P A R A B E N S!\nvocê acertou!\nVocê precisou de {num_tentativas} tentativas!""")
            print(" ")
            print(" --------------------------------------- ")
            repetir = int(input("Você deseja reiniciar o jogo? (Digite 1 para SIM e 0 para NÃO): "))

            break

#aviso de que o valor iserido não é valido

        else:
            if tentativa < 1000 or tentativa > 9999:
                print("")
                print(" --------------------------------------- ")
                print(" ")
                print(f"Sua tentativa nesta rodada foi: {tentativa}")
                print(">>> ATENÇÃO!!! <<<\nO numero deve ser entre >>>1000 e 9999<<<")
                num_tentativas -= 1
                tentativas_restantes += 1

            else:

#operações matematicas que dividem o codigo em unidades

                codigo_1 = codigo // 1000
                codigo_2 = (codigo % 1000) // 100
                codigo_3 = (codigo % 100) // 10
                codigo_4 = codigo % 10

                tentativa_1 = tentativa // 1000
                tentativa_2 = (tentativa % 1000) // 100
                tentativa_3 = (tentativa % 100) // 10
                tentativa_4 = tentativa % 10

                print(" ")
                print(" --------------------------------------- ")
                print(" ")

#comparação das casas com os codigos que permite que seja impresso na tela as casas corretas

                print(" ")

                if num_tentativas < 10:
                    print(f"Sua tentativa nesta rodada foi: {tentativa}")
                    print(" ")
                    print("Acertos: ", end="")
                    
                    if codigo_1 == tentativa_1:
                        print(codigo_1, end="")
                        cont_t += 1 #contador de acerto
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

                    print(" ")
                    print(f"Você acertou > {cont_t} < digitos nesta tentativa.")
                    print(f"Você ERROU! Você ainda tem >>> {tentativas_restantes} <<< tentativas restantes")
                    cont_t -= cont_t

#sistema de dicas para o jogador
                
                if num_tentativas >= 5:
                        print("Dica: ", end="")
                        dica_valida = 0 #variavel para verificar se a dica é valida
                        while dica_valida == 0:
                            slot_dica = random.randint(1, 4) #gera um numero aleatorio que decide qual slot de dica sera impresso
                            rand_dica = random.randint(1, 2) #gera um numero aleatorio que decide qual dica dar
                            
                            if slot_dica == 1:
                                if codigo_1 != tentativa_1:
                                    dica_valida = 1 #verifica se a dica é valida
                                    if rand_dica == 1:
                                        if (codigo_1 % 2 == 0):
                                            print("O primeiro digito é > PAR <")
                                        else:
                                            print("O primeiro digito é > IMPAR <")
                                    else:
                                        if (codigo_1 > tentativa_1):
                                            print(f"O primeiro digito é maior que {tentativa_1}")
                                        else:
                                            print(f"O primeiro digito é menor que {tentativa_1}")
                                else:
                                    dica_valida = 0 #retorna no inicio do loop quando a dica é invalida
                            else:
                                if slot_dica == 2:
                                    if codigo_2 != tentativa_2:
                                        dica_valida = 1 #verifica se a dica é valida
                                        if rand_dica == 1:
                                            if (codigo_2 % 2 == 0):
                                                print("O segundo digito é > PAR <")
                                            else:
                                                print("O segundo digito é > IMPAR <")
                                        else:
                                            if (codigo_2 > tentativa_2):
                                                print(f"O segundo digito é maior que {tentativa_2}")
                                            else:
                                                print(f"O segundo digito é menor que {tentativa_2}")
                                    else:
                                        dica_valida = 0 #retorna no inicio do loop quando a dica é invalida          
                                else:
                                    if slot_dica == 3:
                                        if codigo_3 != tentativa_3:
                                            dica_valida = 1 #verifica se a dica é valida
                                            if rand_dica == 1:
                                                if (codigo_3 % 2 == 0):
                                                    print("O terceiro digito é > PAR <")
                                                else:
                                                    print("O terceiro digito é > IMPAR <")
                                            else:
                                                if (codigo_3 > tentativa_3):
                                                    print(f"O terceiro digito é maior que {tentativa_3}")
                                                else:
                                                    print(f"O terceiro digito é menor que {tentativa_3}")
                                        else:
                                            dica_valida = 0 #retorna no inicio do loop quando a dica é invalida
                                    else:
                                        if slot_dica == 4:
                                            if codigo_4 != tentativa_4:
                                                dica_valida = 1 #verifica se a dica é valida
                                                if rand_dica == 1:
                                                    if (codigo_4 % 2 == 0):
                                                        print("O quarto digito é > PAR <")
                                                    else:
                                                        print("O quarto digito é > IMPAR <")
                                                else:
                                                    if (codigo_4 > tentativa_4):
                                                        print(f"O quarto digito é maior que {tentativa_4}")
                                                    else:
                                                        print(f"O quarto digito é menor que {tentativa_4}")
                                            else:
                                                dica_valida = 0 #retorna no inicio do loop quando a dica é invalida

#aviso de que o jogador errou todas as tentativas
                    
                        else:
                            if num_tentativas == 0:
                                print(" --------------------------------------- ")
                                print(f"Sua tentativa nesta rodada foi: {tentativa}")
                                print(f"O numero de tentativas >>> ACABARAM! <<<\nO codigo correto era >>> {codigo} <<<")
                                print(" ")
                                print(" --------------------------------------- ")
                                repetir = int(input("Você deseja reiniciar o jogo? (Digite 1 para SIM e 0 para NÃO): "))

#loop para impedir respostas alem de 0 ou 1

    if repetir != 1 and repetir != 0: #seleção de resposta invalida
        while repetir != 1 and repetir != 0: #loop para impedir respostas alem de 0 ou 1
            print(" ")
            print("""Responda >> APENAS << com >> 1 ou 0 << 
(1 para SIM e 0 para NÃO)""")
            print(" ")
            repetir = int(input("Você deseja reiniciar o jogo? (Digite 1 para SIM e 0 para NÃO): "))
