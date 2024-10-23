12# Solicita ao usuário para inserir um número
numero = int(input("Digite um número inteiro: "))

# Lista para armazenar os divisores
divisores = []

# Loop para encontrar divisores
for i in range(1, numero + 1):
    if numero % i == 0:  # Verifica se 'i' é um divisor de 'numero'
        divisores.append(i)  # Adiciona o divisor à lista

# Exibe os divisores
print(f"Os divisores de {numero} são: {divisores}")