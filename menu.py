
def menu_principal():
    print("""
╔══════════════════════════════════════════════╗
║      SISTEMA DE PEDIDOS - BUENO'S STORE      ║
╠══════════════════════════════════════════════╣
║  [1] - Cadastrar Produto                     ║
║  [2] - Criar pedido                          ║
║  [3] - Listar pedidos                        ║
║  [4] - Consultar pedidos                     ║
║  [5] - Alterar status do pedido              ║
║  [6] - Sair                                  ║
╠══════════════════════════════════════════════╣
""")
    while True:
        try:
            escolha_usuario = int(input("║  Escolha uma opção: "))
            
        except ValueError:
            print('Digite apenas números! [1 a 5]')
            continue
        
        if  1 <= escolha_usuario <= 6:
            print("╚══════════════════════════════════════════════╝")
            return escolha_usuario
        else:
            print('Digite apenas opções válidas! ')

  
       
        
    