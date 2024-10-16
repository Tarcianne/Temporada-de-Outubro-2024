#Programa que simule um caixa eletrônico
#Definindo o limite de saque
limite_saque=500.00
while True:
#Loop infinito até um valor válido seja fornecido
#Solicita o  valor do saque
 valor_saque=float(input("Digite o  valor do saque(até R$500): R$"))
#Verifica se o valor esta dentro do limite
 if 0 < valor_saque <=limite_saque:
  print(f"Saque de R${valor_saque:.2f} realizado com sucesso!")
  break
#Sai do loop se o valor for inválido
 else:
  print(f"Valor inválido! O valor deve ser maior que R$ O,O e menor ou igual a R${limite_saque}.")

