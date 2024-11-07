lista_bolos = [[10, "João", 12, "sim"], [20, "Manuel", 8, "sim"],
               [12, "José", 15, "não"], [18, "Maria", 11, "sim"],
               [13, "Mara", 13, "não"], [21, "Mara", 9, "não"],
               [17, "Lucy", 17, "não"]]

flag_programa = True

while flag_programa:
  print("\n=== Menu ===")
  print("1. Adicionar bolos")
  print("2. Exibir valor dos bolos")
  print("3. Quantidade de bolos não entregues")
  print("4. Registrar entrega de um bolo")
  print("5. Sair")

  escolha = input("Escolha uma opção (1/2/3/4/5): ")

  if escolha == '1':

    continua_adicionando = True
    while continua_adicionando:
      num_identificacao = int(
          input("Digite o número de identificação do bolo: "))
      nome_cliente = input("Digite o nome do cliente: ")
      peso = int(input("Digite o peso do bolo em quilos: "))
      entregue = input("O bolo foi entregue ao cliente? (sim/não): ").lower()

      lista_bolos.append([num_identificacao, nome_cliente, peso, entregue])

      resposta = input("Deseja adicionar mais bolos? (sim/não): ").lower()
      if resposta != 'sim':
        continua_adicionando = False

  elif escolha == '2':

    print("\nNúmero de Identificação  Valor")
    for bolo in lista_bolos:
      num_identificacao = bolo[0]
      peso = bolo[2]
      valor = peso * 50
      print(f"{num_identificacao}                     R$ {valor:.2f}")

  elif escolha == '3':
    # Quantidade de bolos não entregues
    count = 0
    for bolo in lista_bolos:
      if bolo[3] == "não":
        count += 1
    print(f"\nQuantidade de bolos não entregues: {count}")

  elif escolha == '4':
    # Registrar entrega de um bolo
    num_identificacao = int(
        input("Digite o número de identificação do bolo a ser entregue: "))
    bolo_encontrado = False

    for bolo in lista_bolos:
      if bolo[0] == num_identificacao:
        bolo_encontrado = True
        if bolo[3] == "não":
          print("Entrega registrada com sucesso!")
          bolo[3] = "sim"
        else:
          print("Este bolo já foi entregue anteriormente.")

    if not bolo_encontrado:
      print("Bolo não encontrado na lista.")

  elif escolha == '5':

    print("Saindo do programa...")
    flag_programa = False

  else:

    print("Opção inválida. Escolha novamente.")