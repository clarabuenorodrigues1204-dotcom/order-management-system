def buscar_pedidos(consulta, lista_pedidos):
                                     
    #Mostra o pedido encontrado
    
    for n_pedido in lista_pedidos:
        
        if consulta == n_pedido['Nº do pedido']:
            return n_pedido
       
            
    return None
