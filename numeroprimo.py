def eh_primo(numero):
    if numero <=1:
        return False
    for i in range(2, int(numero**0.5)+1):
        if numero %i==0:
            return False
        return True
    numero_inserido=int(input("Digite um número inteiro:"))
    if eh_primo(numero_inserido):
        print(f"{numero_inserido} é um número primo.")
    else:
        print(f"{numero_inserido} não é um número primo.")
