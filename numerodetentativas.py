def adivinhar_numero():
 numero_predefinido=978
 tentativas=0 
 while True:
  tentativa=int(input("Adivinhe o número!(entre 1 e 100):"))
  tentativas+=1
  if tentativa==numero_predefinido:
   print(f"Parabéns! Você avertou! Era o número {numero_predefinido}!")
   break
  else:
   print("Tente novamente!")
   print(f"Você fez {tentativas} tentativas.")
adivinhar_numero()