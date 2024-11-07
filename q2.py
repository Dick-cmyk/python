lista_palavras = []

contador = 0

while contador < 500:
    palavra = input(f"Digite a {contador + 1}ª palavra: ")
    lista_palavras.append(palavra)
    contador += 1

ultima_palavra = lista_palavras[-1]
contador_ultima_palavra = lista_palavras.count(ultima_palavra)
print(f"A última palavra '{ultima_palavra}' aparece {contador_ultima_palavra} vezes na lista.")

posicao = 0
posicoes_pipoca = []
while posicao < len(lista_palavras):
    if lista_palavras[posicao] == "pipoca":
        posicoes_pipoca.append(posicao)
    posicao += 1

if posicoes_pipoca:
    print("Posições onde 'pipoca' foi inserida:", posicoes_pipoca)
else:
    print("A palavra 'pipoca' não foi inserida na lista.")

primeiras_10_posicoes = []
posicao = 0
while posicao < 10 and posicao < len(lista_palavras):
    primeiras_10_posicoes.append(lista_palavras[posicao])
    posicao += 1

print("Conteúdo das 10 primeiras posições da lista:")
print(primeiras_10_posicoes)

posicao = int(input("Digite uma posição para consultar a palavra: "))
if 0 <= posicao < len(lista_palavras):
    palavra_posicao = lista_palavras[posicao]
    print(f"A palavra na posição {posicao} é: {palavra_posicao}")
else:
    print("Posição inválida.")

palavra_buscar = input("Digite uma palavra para verificar sua frequência na lista: ")
quantidade_palavra = 0
posicao = 0
while posicao < len(lista_palavras):
    if lista_palavras[posicao] == palavra_buscar:
        quantidade_palavra += 1
    posicao += 1

if quantidade_palavra > 0:
    print(f"A palavra '{palavra_buscar}' aparece {quantidade_palavra} vezes na lista.")
else:
    print(f"A palavra '{palavra_buscar}' não foi encontrada na lista.")