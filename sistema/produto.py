def cadastrar_produto(catalogo_produtos):
    
    produto = {}
    produto['Nome'] = input('Nome do produto: ').strip().title()
    
    while True:
        
        try:
            produto['Quantidade em estoque'] = int(input('Quantidade de produto no estoque: '))
            
            produto['Valor'] = float(input('Valor do produto: '))
            
            produto['Categoria'] = input('Categoria do produto: ').strip().capitalize()  
            
            if produto['Quantidade em estoque'] <= 0 :
                produto['Quantidade em estoque'] = int(input('ERRO! Digite novamente. Quantidade de produto no estoque: '))
                
            elif produto['Valor'] <= 0:
                produto['Valor'] = float(input('ERRO! Digite novamente. Valor do produto: '))
                  
        
        except ValueError:
            
            print('Somente números! Tente novamente')
            continue
        
        catalogo_produtos.append(produto.copy())       
        
        print('Produto cadastrado com sucesso!')
        
        break

def menu_produtos(catalogo_produtos):
    
    for num, produto in enumerate(catalogo_produtos, start=1):

        print("═" * 48)
        print(f"PRODUTO {num}º")
        print("═" * 48)

        print(f'Nome: {produto["Nome"]}')
        print(f'Categoria: {produto["Categoria"]}')
        print(f'Quantidade em estoque: {produto["Quantidade em estoque"]}')
        print(f'Valor: R$ {produto["Valor"]:.2f}')

        print("═" * 48)
        
   

