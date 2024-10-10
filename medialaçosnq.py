#Iniciando a soma das notas
soma=0
quantidade_notas= 3

#Solicita as notas ao usuário
for i in range(1,quantidade_notas+1):
    nota=float(input(f"Digite a nota{i}:"))
    soma+=nota

#Adiciona a nota à soma
#Calcula a média
media=soma/quantidade_notas

#Exibe a média
print(f"A média das {quantidade_notas} notas é:{media:.2f}")