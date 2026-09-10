
def menu_principal():
    print("""
╔══════════════════════════════════════════════╗
║      SISTEMA DE PEDIDOS - BUENO'S STORE      ║
╠══════════════════════════════════════════════╣
║  [1] - Criar pedido                          ║
║  [2] - Listar pedidos                        ║
║  [3] - Consultar pedidos                     ║
║  [4] - Alterar status do pedido              ║
║  [5] - Sair                                  ║
╠══════════════════════════════════════════════╣
""")
    while True:
        try:
            escolha_usuario = int(input("║  Escolha uma opção: "))
            
        except ValueError:
            print('Digite apenas números! [1 a 5]')
            continue
        
        if  1 <= escolha_usuario <= 5:
            print("╚══════════════════════════════════════════════╝")
            return escolha_usuario
        else:
            print('Digite apenas opções válidas! ')

  
       
        
    