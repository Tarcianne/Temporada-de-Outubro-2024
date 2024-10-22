import random

numero_secreto= random.randint(1,100)

print("Bem-vindo jogador!, este é o jogo da adivinhação, vamos começar!")
print("Está preparado?")
print("Eu tenho um número entre 1 e 100")
print("Vamos! Tente adivinhá-lo!")

while True:
    palpite=int(input("Digite seu palpite:"))
    if palpite<numero_secreto:
        print("Muito baixo!")
        print("Vamos lá! Tente novamente!")
    elif palpite>numero_secreto:
        print("Ahhhhhhh!")
        print("Você errou! Número muito alto!")
        print("Tente novamente!")
    else:
        print("Parabéns! Você acertou!")
        print("Até a próxima jogador!")