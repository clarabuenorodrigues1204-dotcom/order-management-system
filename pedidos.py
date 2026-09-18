from os import system
system('cls')

import produto
import ficha_cliente
import buscar_pedidos
import mostra_ficha
#Criação de Pedidos

def criar_pedidos(lista_pedidos, catalogo_produtos):
    
    from random import randint

    pedido = {}
    pedidos_comprados = []

    #Gerador de ID do pedido

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

    #Cadastro do cliente
    
    pedido["Nº do pedido"] = numero_pedido

    ficha_cliente.ficha_cliente(pedido)

    while True:
        try:
            quant_produtos = int(input("Quantos produtos serão adicionados ao pedido? "))

            if quant_produtos <= 0:
                print("ERRO! A quantidade deve ser maior que zero.")
                continue
            
            break
        
        except ValueError:
            print("APENAS NÚMEROS!")
            
    #Adição de produto ao pedido       

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

#Lista os pedidos cadastrados no sistema
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

#Consulta um pedido específico utilizando o ID gerado
def consultar_pedido(lista_pedidos):
    #Verifica se o ID dado pelo usuário existe na lista, e verifica se o que foi digitado é um número ou não
    while True:
        try:
            consulta = int(input('Insira o Nº do pedido: '))
            
        except ValueError:
            print('Digite apenas números!')
            continue
        
        pedido = buscar_pedidos.buscar_pedidos(consulta, lista_pedidos)
               
        if pedido != None:            
            mostra_ficha.mostra_ficha(pedido)
            break
                       
#Altera o status do pedido que começa com o status "pendente"
def alterar_status(lista_pedidos):
    #Verifica se o ID dado pelo usuário existe na lista, e verifica se o que foi digitado é um número ou não
    while True:
        try:
            consulta = int(input('Insira o número do pedido: '))
            
        except ValueError:
            
            print('Digite apenas números!')
            continue

        pedido = buscar_pedidos.buscar_pedidos(consulta,lista_pedidos)

        if pedido != None:
            mostra_ficha.mostra_ficha(pedido)
            continue
        
        escolha_alterar = input('Deseja alterar o status do pedido? [S/N] ').strip().upper()

        while escolha_alterar != 'S' and escolha_alterar != 'N':
            
            escolha_alterar = input('Digite apenas [S/N]. Deseja alterar o status do pedido? ').strip().upper()

        if escolha_alterar == 'N':
            return
        #Opções de status para ser alterado
        print("""PARA QUAL STATUS SERÁ ALTERADO:
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
            pedido['Status'] = 'Pendente'

        elif escolha_usuario == 2:
            pedido['Status'] = 'Preparando'

        elif escolha_usuario == 3:
            pedido['Status'] = 'Enviado'

        elif escolha_usuario == 4:
            pedido['Status'] = 'Entregue'

        print('Status alterado com sucesso!')
        return
    
    