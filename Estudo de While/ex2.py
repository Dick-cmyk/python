cont = 0
contMais50 = 0
somaGastos = 0
while cont < 5:
  cont = cont + 1
  qt = int(input("Quantidade:"))
  preco = float(input("Preço unitário"))
  gasto = qt * preco
  print("Valor gasto com o produto",cont,"foi",gasto)
  if preco > 50:
    contMais50 = contMais50 + 1
    somaGastos = somaGastos + gasto
    print("n\Quant. de produtos que custam mais que R$ 50.00", contMais50)
    print("O total geral gasto:",somaGastos)