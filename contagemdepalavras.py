def contar_palavras(frase):
    # Divide a frase em palavras usando o espaço como delimitador
    palavras = frase.split()
    return len(palavras)

def main():
    # Pede ao usuário para inserir uma frase
    frase_usuario = input("Por favor, insira uma frase: ")
    
    # Conta as palavras na frase
    numero_de_palavras = contar_palavras(frase_usuario)
    
    # Exibe o resultado
    print(f"A sua frase tem {numero_de_palavras} palavras.")

if __name__ == "_main_":
    main()