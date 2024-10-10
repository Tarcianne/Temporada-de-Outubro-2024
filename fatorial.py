#Solicita ao usuário um nuḿero inteiro
numero=int(input("Digite um número inteiro para calcular o fatorial:"))

#Inicializa a variável para o fatorial
fatorial=1

#Calcula o fatorial usando um laço
for i in range(1,numero+1):
    fatorial*=i
#Multiplica fatorial pelo número atual
#Exibe resultado
print(f"O fatorial de {numero} é: {fatorial}")