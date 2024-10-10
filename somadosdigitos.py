#Solicita ao usuário um número inteiro
numero=input("Digite um número inteiro:")

#Inicializa a soma dos dígitos 
soma_digitos=0

#Calcula a soma dos dígitos usando um laço
for digito in numero:
    if digito.isdigit():

#Verifica se o caractere é um dígito
     soma_digitos+=int(digito)

#Converte o dígito para inteiro e adiciona À soma
#Exibe o resultado
print(f"A soma dos dígitos de {numero} é:{soma_digitos}")