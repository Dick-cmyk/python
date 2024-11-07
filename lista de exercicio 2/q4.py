Aluguel = 500

custo = int(input("Qual foi o preço de custo dos pães de mel comprados:"))
venda = int(input("Qual foi o preço de venda dos pães de mel comprados:"))
total_1 = int(input("Quantos pães de mel foram comprados para venda:"))
total_2 = int(input("Quantos pães de mel foram vendidos na feira gastronomica:"))

total_comprado = total_1 * custo
total_vendido = total_2 * venda

lucro_vendas = total_vendido - total_comprado
lucro_total = lucro_vendas - Aluguel
print("O seu lucro obtido na feira foi de R$",lucro_total)














