#Programa que multiplica dois números sem usar a operação *

#Função para a multiplicação
def multiplicar(num1, num2):
 resultado=0

#Laço 
 for _ in range(num2):
  resultado += num1

#Soma do num1 ao resultado
 return resultado

#Retorna o resultado da multiplicação
#Entrada do usuário
num1=int(input("Insira o primeiro número:"))
num2=int(input("Insira o segundo número:"))

#Chama a funçaõ de multiplicação e exibe o resultado
resultado_final= multiplicar(num1, num2)
print(f"O resultado de {num1} multplicado por {num2} é {resultado_final}.")
