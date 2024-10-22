#Programa que exibe o  quadrado de todos os números de 1 a 10 usando o laço while
while True:

#Inicia um loop infinito
 num=int(input("Insira um número entre 1 a 10:"))

#Pede ao usuário para inserir um número e se ele está dentro do intervalo permitido
 if 1<=num<=10:
  quadrado=num**2
 else:
  print("Por favor, insira um número válido!")

#Calculando o quadrado
 print(f"O quadrado de {num} é {quadrado}.")

#Exibe o resultado 
 break

#Sai do loop se o número for válido
