from os import system
system('cls')

import menu
import pedidos
import produto

lista_pedidos = []
catalogo_produtos = []

def main():
    while True:
        escolha = menu.menu_principal()
        
        if escolha == 1:
            produto.cadastrar_produto(catalogo_produtos)
            
        if escolha == 2:
            pedidos.criar_pedidos(lista_pedidos, catalogo_produtos)
            
        if escolha == 3:
            pedidos.listar(lista_pedidos)
        
        if escolha == 4:
            pedidos.consultar_pedido(lista_pedidos)
        
        if escolha == 5:
            pedidos.alterar_status(lista_pedidos)
            
        if escolha == 6:
            print('Fim do programa')
            break
    
main()
