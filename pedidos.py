from os import system
system('cls')

import produto

def criar_pedidos(lista_pedidos, catalogo_produtos):
    
    from random import randint

    pedido = {}
    pedidos_comprados = []

    numero_pedido = randint(100000, 999999)
  
    while True:
        numero_repetido = False

        for pedido_cadastrado in lista_pedidos:
            
            if pedido_cadastrado["Nº do pedido"] == numero_pedido:
                numero_repetido = True
                break

        if numero_repetido:
            numero_pedido = randint(100000, 999999)

        else:
            break


    pedido["Nº do pedido"] = numero_pedido

    pedido["Cliente"] = input("Digite o nome do(a) cliente: ").title().strip()

    while True:
        try:
            quant_produtos = int(input("Quantos produtos serão adicionados ao pedido? "))

            if quant_produtos <= 0:
                print("ERRO! A quantidade deve ser maior que zero.")
                continue
            
            break
        
        except ValueError:
            print("APENAS NÚMEROS!")

    for _ in range(quant_produtos):
        
        while True:
            
            try:
                produto.menu_produtos(catalogo_produtos)
                escolha_user = int(input("Quais produtos deseja adicionar ao pedido? "))
            
                if escolha_user < 1 or escolha_user > len(catalogo_produtos):
                    print("Produto inexistente!")
                    continue

                break
                            
            except ValueError:
                print('APENAS NÚMEROS')
                continue
            

        produtos_escolhidos = catalogo_produtos[escolha_user - 1]

        pedidos_comprados.append(produtos_escolhidos.copy())

    for item in pedidos_comprados:
        pedido["Lista de produtos"] = item["Nome"]

    pedido["Status"] = "Pendente"

    lista_pedidos.append(pedido.copy())

    print("Pedido cadastrado com sucesso!")


def listar(lista_pedidos):

    if len(lista_pedidos) == 0:
        print("Nenhum pedido cadastrado.")
        return

    for indice, pedido in enumerate(lista_pedidos, start=1):
        print("═" * 48)
        print(f" PEDIDO {indice}")
        print("═" * 48)
        print(f" Nº do pedido: {pedido['Nº do pedido']}")
        print(f" Cliente:      {pedido['Cliente']}")
        print(f" Produtos:     {pedido['Lista de produtos']}")
        print(f" Status:       {pedido['Status']}")
        print("═" * 48)

def consultar_pedido(lista_pedidos):
    while True:
        try:
            consulta = int(input('Insira o Nº do pedido: '))
            
        except ValueError:
            print('Digite apenas números!')
            continue
        
        pedido_encontrado = False
        
        for n_pedido in lista_pedidos:
            
            if consulta == n_pedido['Nº do pedido']:
                
                pedido_encontrado = True
                
                print("═" * 48)
                print(f" PEDIDO Nº {n_pedido['Nº do pedido']}")
                print("═" * 48)
                print(f" Cliente:   {n_pedido['Cliente']}")
                print(f" Produtos:  {', '.join(n_pedido['Lista de produtos'])}")
                print(f" Status:    {n_pedido['Status']}")
                print("═" * 48)
                
                break
            
        if pedido_encontrado:
            break
        print('Não há pedido com esse número! Tente novamente')  

def alterar_status(lista_pedidos):

    while True:

        try:
            consulta = int(input('Insira o número do pedido: '))
        except ValueError:
            print('Digite apenas números!')
            continue

        pedido_encontrado = False

        for n_pedido in lista_pedidos:

            if consulta == n_pedido['Nº do pedido']:
                pedido_encontrado = True

                print("═" * 48)
                print(f" PEDIDO Nº {n_pedido['Nº do pedido']}")
                print("═" * 48)
                print(f" Cliente:   {n_pedido['Cliente']}")
                print(f" Produtos:  {n_pedido['Lista de produtos']}")
                print(f" Status:    {n_pedido['Status']}")
                print("═" * 48)

                break

        if not pedido_encontrado:
            print('Não há pedido com esse número! Tente novamente.')
            continue

        escolha_alterar = input(
            'Deseja alterar o status do pedido? [S/N] '
        ).strip().upper()

        while escolha_alterar != 'S' and escolha_alterar != 'N':
            escolha_alterar = input(
                'Digite apenas [S/N]. Deseja alterar o status do pedido? '
            ).strip().upper()

        if escolha_alterar == 'N':
            return

        print("""
PARA QUAL STATUS SERÁ ALTERADO:

[1] - Pendente
[2] - Preparando
[3] - Enviado
[4] - Entregue
""")

        while True:

            try:
                escolha_usuario = int(input('Escolha uma opção: '))
            except ValueError:
                print('Digite apenas números!')
                continue

            if 1 <= escolha_usuario <= 4:
                break
            else:
                print('Digite apenas opções válidas!')

        if escolha_usuario == 1:
            n_pedido['Status'] = 'Pendente'

        elif escolha_usuario == 2:
            n_pedido['Status'] = 'Preparando'

        elif escolha_usuario == 3:
            n_pedido['Status'] = 'Enviado'

        elif escolha_usuario == 4:
            n_pedido['Status'] = 'Entregue'

        print('Status alterado com sucesso!')
        return
    
    