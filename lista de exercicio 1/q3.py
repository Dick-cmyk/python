custo_por_quilo = 30.00
peso_prato_vazio = 0.2

peso_prato_cheio = float(input("Qual o valor (em quilo) que deu seu prato cheio?"))
peso_refeição = peso_prato_cheio - peso_prato_vazio

valor_a_pagar = peso_refeição * custo_por_quilo
print("O valor que o senhor terá que pagar sera de R$",valor_a_pagar)



