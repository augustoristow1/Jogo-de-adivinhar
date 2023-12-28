print("***********************************")
print("Bem vindo ao jogo de adivinhação!")
print("***********************************")


numero_secreto = 42

chute_string = input("Digite o seu número:")
chute = int(chute_string)

print("Você digitou", chute_string)

if(numero_secreto == chute):
    print("Você acertou!")
else:
    print("Você errou!"); 
