def ficha_cliente(pedido):
    pedido["Cliente"] = input('Digite o nome do(a) cliente: ').title().strip()
    pedido["CPF"] = input('CPF: ')
    pedido["Data de Nascimento"] = input('Data de nascimento: ').strip()
    pedido["Email"] = input('E-mail: ').strip()
    pedido["Telefone"] = input('Telefone: ').strip()
    pedido["Endereço"] = input('Endereço: ').strip()
    pedido["Cidade"] = input('Cidade: ').strip()
    pedido["Estado"] = input('Estado: ').strip()