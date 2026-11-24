def mostra_ficha(pedido):
    print("╔" + "═" * 58 + "╗")
    print("║" + "DETALHES DO PEDIDO".center(58) + "║")
    print("╠" + "═" * 58 + "╣")

    print(f"║   Nº DO PEDIDO: {pedido['Nº do pedido']:<41}║")

    print("╠" + "═" * 58 + "╣")
    print("║  DADOS DO CLIENTE" + " " * 40 + "║")
    print("║" + " " * 58 + "║")

    print(f"║  Cliente:     {pedido['Cliente']:<42} ║")
    print(f"║  CPF:         {pedido['CPF']:<42}║")
    print(f"║  E-mail:      {pedido['Email']:<42}║")
    print(f"║  Telefone:    {pedido['Telefone']:<42}║")
    print(f"║  Endereço:    {pedido['Endereço']:<42}║")
    print(f"║  Cidade:      {pedido['Cidade']:<42}║")
    print(f"║  Estado:      {pedido['Estado']:<42}║")

    print("╠" + "═" * 58 + "╣")
    print("║ PRODUTOS" + " " * 48 + "║")
    print("║" + " " * 58 + "║")

    for numero, produto in enumerate(pedido["Lista de produtos"], start=1):
        print(f"║  {numero:02}. {produto:<51}║")

    print("╠" + "═" * 58 + "╣")
    print(f"║  STATUS: {pedido['Status']:<48}║")
    print("╚" + "═" * 58 + "╝")