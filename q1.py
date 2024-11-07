quantidade_habitantes = int(input("Digite a quantidade de habitantes que responderam à pesquisa: "))

idade_mais_velho = -1
sexo_mais_velho = ""

contador_mulheres_idosas = 0
contador_jovens = 0

contador = 0
while contador < quantidade_habitantes:
    idade = int(input(f"Informações da {contador + 1}ª pessoa:\nIdade: "))
    sexo = input("Sexo (M/F): ").upper()
    nacionalidade = input("Nacionalidade (Brasileiro/Estrangeiro): ").lower()

    if sexo == 'M' and idade >= 18 and nacionalidade == 'brasileiro':
        print("Deve se alistar ou já se alistou no serviço militar.")

    if sexo == 'F' and nacionalidade == 'brasileiro' and idade >= 65:
        contador_mulheres_idosas += 1

    if idade > idade_mais_velho:
        idade_mais_velho = idade
        sexo_mais_velho = sexo

    if 15 <= idade <= 29:
        contador_jovens += 1

    contador += 1

if sexo_mais_velho == 'M':
    print("O sexo da pessoa mais velha é masculino.")
elif sexo_mais_velho == 'F':
    print("O sexo da pessoa mais velha é feminino.")

percentual_jovens = contador_jovens / quantidade_habitantes
if percentual_jovens >= 0.5:
    print("Pelo menos metade dos habitantes é jovem.")
else:
    print("Menos da metade dos habitantes é jovem.")

print(f"Quantidade de mulheres brasileiras idosas (65 anos ou mais): {contador_mulheres_idosas}")