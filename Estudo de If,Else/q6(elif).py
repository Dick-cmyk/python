nota1 = float(input("Qual foi a nota da sua primeira prova:"))
nota2 = float(input("Qual foi a nota da sua segunda prova:"))

media = (nota1 + nota2) / 2
print("A média é:",media)

if media >= 6.0:
  print("Você foi aprovado!")
elif media >= 4.0:
  print("Você terá que fazer o exame!")
  notaExame = float(input("Qual foi sua nota no exame:"))
  if notaExame >= 6.0:
    print("Você foi aprovado no exame!")
  else:
    print("Você foi reprovado no exame!")

else:
  print("Você foi reprovado!")