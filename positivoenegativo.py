#Programa que pede um número positivo até que o usuário insira um número negativo
def eh_numero(val):

#Verifica se a string pode ser convertida para um número

  if val.replace('.','',1).isdigit()or(val.startswith('-') and val[1:].replace('.','',1).isdigit()):
      return True
  return False

while True:
    numero=input("Digite um número positivo(ou negativo para sair):")
    
    if eh_numero(numero):
       numero=float(numero)
       if numero <0:
          print("Você digitou um número negativo. Saindo do programa.")
          break
       elif numero>=0:
          print(f"Você digitou: {numero}. Continue!")
       else:
          print("Por favor, digite um número válido.")