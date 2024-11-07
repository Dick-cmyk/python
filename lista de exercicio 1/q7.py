preco_pacote_lapis = 8.00
preco_pacote_caneta = 6.50

quantidade_pacote_lapis = int(input("Digite a quantidade de pacotes de lapis comprados:"))
quantidade_pacote_canetas = int(input("Digite a quantidade de pacotes de canetas compradas:"))

valor_total_lapis = quantidade_pacote_lapis * preco_pacote_lapis
valor_total_canetas = quantidade_pacote_canetas * preco_pacote_caneta

valor_total = valor_total_lapis + valor_total_canetas
print("O valor total a ser pago é: R$",valor_total)