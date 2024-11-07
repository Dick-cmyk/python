somaIdades = 0
qtPessoas = 0

idade = int(input("Digite a sua idade:"))
while idade > 0:
  sexo = input("Sexo:")
  somaIdades = somaIdades + idade
  qtPessoas = qtPessoas + 1
  idade = int(input("Digite a idade:"))
  print("Média das idades:",somaIdades / qtPessoas)