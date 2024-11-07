pcd = input("Tem alguma deficiência física?(sim ou não)")
id = int(input("Qual sua idade:"))

if pcd == 'sim' or id >=65:
  print("Você terá atendimento prioritário!")
else:
  print("Você terá atendimento normal!")