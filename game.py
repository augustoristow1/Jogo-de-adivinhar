print ("***********************************")
print(" Bem vindo ao jogo de adivinhar ")
print  ("***********************************")

numero_secreto = 42
total_de_tentativas = 3 # usando range para ficar com 3

                                                #O último numero da rodada é nulo, considerado o final, então aumente +1
                                                # a função range é usada para fazer um LAÇO
for rodada in range(1, total_de_tentativas + 1):         # range define a serie de valores
    print("Tentativa, {} de {}" .format( rodada, total_de_tentativas))

    chute_str = input(" Digite o seu numero:")
    print("Você digitou ", chute_str)
    chute = int(chute_str)

                                    #String Intrepolation ( .format ) 'e usado para formatar
                                    # {} é usado para representar um valor/numeração

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Você acertou!") #caso acerte de primeira usamos "break" para para o código
        break 
    else:
        if(maior):
            print("Você errou! O seu chute foi maior que o número secreto")
        elif(menor):
            print("Você errou! O seu chute foi menor que o número secreto")



    
print("Fim de jogo")




# para função de loop/laço usar "For ... range"

