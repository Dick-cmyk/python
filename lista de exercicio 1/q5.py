preco_clip_plastico = 5.00
preco_clip_metal = 10.00

quantidade_caixas_plastico = int(input("Digite a quantidade  de caixas vendidas de clips de plastico:"))
quantidade_caixas_metal = int(input("Digite a quantidade de caixas vendidas de clips de metal:"))

valor_arrecadado_plastico = quantidade_caixas_plastico * preco_clip_plastico
valor_arrecadado_metal = quantidade_caixas_metal * preco_clip_metal

valor_total_arrecadado = valor_arrecadado_plastico + valor_arrecadado_metal
print("Valor arrecadado  com clips de Plástico: R$",valor_arrecadado_plastico)
print("Valor arrecadado com clips de metal: R$",valor_arrecadado_metal)