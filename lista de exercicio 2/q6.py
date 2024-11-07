Custo_de_fabrica = float(input("Digite o custo de fábrica de carros: R$ "))

percentual_distribuidor = 0.28
percentual_impostos = 0.45

valor_distribuidor = Custo_de_fabrica * percentual_distribuidor
valor_impostos = Custo_de_fabrica * percentual_impostos

custo_consumidor = Custo_de_fabrica + valor_distribuidor + valor_impostos
print("O custo ao consumidor é: R$",custo_consumidor)














