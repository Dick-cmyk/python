import random
valorAleatorio = random.randint(1, 10 )

numero1 = int(input("Informe um número entre 1 e 10:"))

if numero1 > valorAleatorio:
  print("O seu número digitado é maior que o valor gerado aleatoriamente.")

elif numero1 < valorAleatorio:
  print("O número digitado é menor que o valor gerado aleatoriamente.")

else:
  print("O numero digitado é igual ao valor gerado aleatoriamente.")










