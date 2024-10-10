#Solicita ao úsuario um números inteiro
numero=int(input("Digite um número inteiro(entre 1 e 10):"))

#Exibe a tabuada do número 
print(f"Tabuada do {numero}:")

for i in range(1,11):
    resultado=numero*i
    print(f"{numero}x{i}={resultado}")