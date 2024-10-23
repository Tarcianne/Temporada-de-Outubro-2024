# Início do loop
while True:
    # Solicita ao usuário para inserir um número
    numero = float(input("Digite um número positivo (ou um número negativo para sair): "))
    
    # Verifica se o número é negativo
    if numero < 0:
        print("Você inseriu um número negativo. O programa será encerrado.")
        break  # Encerra o loop
    
    # Verifica se o número é positivo
    if numero >= 0:
        print(f"Você inseriu o número positivo: {numero}")