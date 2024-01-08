print("***********************************")
print("Bem vindo ao jogo de adivinhação!")
print("***********************************")


numero_secreto = 42

chute_string = input("Digite o seu número:")
chute = int(chute_string)

print("Você digitou", chute_string)

acertou = numero_secreto == chute;
maior = chute > numero_secreto;
menor = chute < numero_secreto;

if(acertou):
    print("Você acertou!")
else:
    if (maior):
        print("Você errou! Seu chute é maior que o número secreto")
    elif (menor):
        print("Você errou! Seu chute é menor que o número secreto")    
print("Fim de jogo"); 


