def fibonacci(n):
    #Função para gerar os N números da série de Fibonacci
    fib_sequence = []
    
    # Verifica se o número de termos solicitados é válido
    if n <= 0:
        print("Por favor, insira um número inteiro positivo.")
        return
    elif n == 1:
        fib_sequence = [0]
    elif n == 2:
        fib_sequence = [0, 1]
    else:
        fib_sequence = [0, 1]
        for i in range(2, n):
            next_number = fib_sequence[i - 1] + fib_sequence[i - 2]
            fib_sequence.append(next_number)
    
    return fib_sequence

def main():
    #Função principal para executar o programa
    try:
        n= int(input("Digite quantos números da série de Fibonacci você gostaria de ver: "))
        result = fibonacci(n)
        
        print(f"A sequência de Fibonacci com {n} números é:")
        print(result)
    
    except ValueError:
        print("Por favor, insira um número inteiro válido.")
if __name__ == "__main__":
 main()
