id = int(input('Idade:'))
sexo = input("Sexo(responda com 'm' ou 'f'):")
if sexo == 'm' and id >= 18:
  print("Deve se alistar!")
else:
  print("Não deve se alistar")