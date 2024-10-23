def inicializar_tabuleiro():
    return [' ' for _ in range(9)]  # Cria um tabuleiro vazio

def mostrar_tabuleiro(tabuleiro):
    print("---------")
    for i in range(3):
        print(f"| {' | '.join(tabuleiro[i*3:(i+1)*3])} |")
        print("---------")

def verificar_ganho(tabuleiro):
    # Checa linhas, colunas e diagonais
    combinacoes = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # linhas
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # colunas
        (0, 4, 8), (2, 4, 6)              # diagonais
    ]
    
    for a, b, c in combinacoes:
        if tabuleiro[a] == tabuleiro[b] == tabuleiro[c] != ' ':
            return True
    return False

def jogo_da_velha():
    tabuleiro = inicializar_tabuleiro()
    jogador_atual = 'X'
    
    for _ in range(9):  # No máximo 9 jogadas
        mostrar_tabuleiro(tabuleiro)
        posicao = int(input(f"Jogador {jogador_atual}, escolha uma posição (1-9): ")) - 1
        
        if tabuleiro[posicao] != ' ':
            print("Posição já ocupada! Tente novamente.")
            continue
        
        tabuleiro[posicao] = jogador_atual
        
        if verificar_ganho(tabuleiro):
            mostrar_tabuleiro(tabuleiro)
            print(f"Jogador {jogador_atual} ganhou!")
            return
        
        # Alterna entre os jogadores
        jogador_atual = 'O' if jogador_atual == 'X' else 'X'
    
    mostrar_tabuleiro(tabuleiro)
    print("O jogo terminou em empate!")

# Inicia o jogo
jogo_da_velha()

