#Inicializa variáveis para soma e contagem
soma=0
contador=0

#Solicita ao usuário a entrada de números
while True:
    entrada=input("Digite um número('fim' para encerrar):")

#Verifica se  o usuário deseja sair do loop
    if entrada.lower()=='fim':
        break


    try:
#Converte a entrada para um númerro e adiciona à soma 
     numero=float(entrada)
     soma+=numero
     contador+=1
    except ValueError:
       print("Por favor,insira um número válido!")

#Verifica se algum número foi inserido antes de calcular a média
if contador>0:
   media=soma/contador
   print(f"A média do número inserido é:{media}")
else:
   print("Nenhum número foi inserido.")