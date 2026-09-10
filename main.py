from os import system
system('cls')

import menu
import pedidos

lista_pedidos = []

def main():
    while True:
        escolha = menu.menu_principal()
        
        if escolha == 1:
            pedidos.criar_pedidos(lista_pedidos)
        
        if escolha == 2:
            pedidos.listar(lista_pedidos)
        
        if escolha == 3:
            pedidos.consultar_pedido(lista_pedidos)
        
        if escolha == 4:
            pedidos.alterar_status(lista_pedidos)
            
        if escolha == 5:
            print('Fim do programa')
            break
    
main()
