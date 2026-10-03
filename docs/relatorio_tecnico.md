# Documentação técnica — Order Management System


## 01 Visão geral

| Aspecto | Descrição |
|---|---|
| Projeto | Order Management System • Bueno’s Store |
| Objetivo | Praticar Python por meio do cadastro de produtos e do gerenciamento de pedidos no terminal. |
| Escopo da documentação | Pontos positivos, problemas encontrados, melhorias de desempenho, extração de funções e proposta visual com Rich. |
| Diagnóstico | A modularização é uma boa base. A prioridade é corrigir validações e fluxos de erro, seguida de persistência e controle de estoque. |
| Estado da entrega | As correções do sistema são propostas. O exemplo Rich é executável, usa dados fictícios e mantém alterações apenas em memória. |
| Data da análise | 24 de setembro de 2026 |

## 02 Pontos positivos

| Ponto positivo | Evidência no projeto | Benefício |
|---|---|---|
| Separação inicial de responsabilidades | Menu, produtos, pedidos, busca e ficha em módulos distintos. | Facilita localizar e evoluir cada parte. |
| Busca reutilizável | buscar_pedidos() recebe dados e retorna o pedido ou None, sem entrada de teclado. | Pode ser usada em outras telas e em testes. |
| Reutilização da ficha | Consulta e alteração de status usam a mesma apresentação. | Reduz repetição de código. |
| Tratamento de entradas | Menus e cadastros tratam ValueError; a criação exige quantidade positiva. | Evita parte dos erros de digitação. |
| Verificação de IDs | A criação procura colisões antes de registrar o número. | Demonstra atenção à identificação única. |
| Dados recebidos por parâmetro | Operações recebem listas de pedidos e de produtos. | Permite exercitar funções com dados temporários. |
| Registro do aprendizado | O projeto documenta seu propósito e as melhorias planejadas. | Ajuda a acompanhar a evolução. |

## 03 Problemas e correções

| Prioridade | Problema | Efeito | Correção proposta |
|---|---|---|---|
| Alta | Pedido inexistente na alteração de status | Confirmar a alteração tenta modificar None e causa TypeError. | Interromper o fluxo após uma busca sem resultado e informar o usuário. |
| Alta | Criação com catálogo vazio | Nenhuma opção é válida e a seleção fica presa no laço. | Verificar o catálogo antes do cadastro do cliente e retornar ao menu. |
| Alta | Validação incompleta de estoque e preço | A segunda entrada não é revalidada; o elif pode pular a validação do preço. | Validar cada campo em um laço próprio e definir se estoque zero é permitido. |
| Alta | Ausência de persistência | As listas são perdidas ao encerrar. O JSON existente não é utilizado. | Carregar e salvar pedidos e catálogo, tratando ausência e conteúdo inválido. |
| Média | Consulta sem retorno claro | Pedido não encontrado não gera mensagem nem oferece cancelamento. | Exibir aviso, tratar lista vazia e permitir voltar. |
| Média | Pedido guarda apenas nomes dos produtos | Não preserva quantidade e preço da compra; não há baixa de estoque. | Criar itens com ID, nome, quantidade e preço unitário; validar antes de confirmar. |
| Média | Campos vazios e valores monetários frágeis | Textos obrigatórios ficam vazios; float aceita valores como nan. | Validar texto e valores finitos; usar Decimal a partir de texto ou centavos inteiros. |
| Média | Execução durante importação | Importar main inicia o programa; alguns módulos limpam a tela com cls. | Proteger a entrada com if __name__ == "__main__" e concentrar ações de terminal na interface. |
| Média | Ausência de suíte automatizada | Mudanças podem reintroduzir os problemas de cadastro e consulta. | Testar casos de erro e, depois, as regras de estoque e persistência. |
| Baixa | Alinhamento manual da ficha | Textos longos ultrapassam a largura das molduras. | Usar tabelas e painéis Rich com quebra de texto. |
| Baixa | Documentação e mensagens desatualizadas | Mensagem limita opções a 1–5, mas o menu aceita 6; endereço já existe e ainda consta como pendência. | Revisar mensagens, estrutura de arquivos e lista de melhorias. |

## 04 Melhorias de performance

| Mudança | Situação atual | Proposta e ganho esperado | Condição |
|---|---|---|---|
| Montar itens uma única vez | A lista de nomes é reconstruída após cada seleção: O(k²). | Inicializar antes do laço e acrescentar só o novo item: O(k). | k é a quantidade de itens do pedido. O ganho refere-se à montagem da lista. |
| Reduzir impressão repetida | Catálogo completo por tentativa e lista acumulada por item. | Remover a saída de depuração; exibir catálogo sob demanda ou paginar. | Imprimir p produtos a cada uma das k escolhas custa O(k × p), fora novas tentativas. |
| Indexar pedidos por número | Cada busca percorre a lista: O(n). | Manter dicionário por número: consulta O(1) em média. | Construção custa O(n). Não reconstruir a cada consulta; manter sincronizado. |
| Verificar IDs com conjunto ou índice | Cada novo sorteio varre os pedidos cadastrados. | Consultar números usados por conjunto ou dicionário. | São 900.000 IDs de seis dígitos. Tratar esgotamento; contador persistido é uma alternativa. |
| Escolher armazenamento conforme o volume | Dados somente em memória. | Começar com persistência simples; avaliar SQLite quando consultas e volume exigirem. | Regravar JSON custa O(n) no tamanho dos dados. A troca não é necessária só por antecipação. |
| Separar organização de velocidade | Menus usam if independentes e misturam entrada, regra e saída. | Usar elif e funções menores para clareza e manutenção. | Isso e a adoção de Rich não representam ganho relevante de tempo por si só. |
| Medir antes de otimizar mais | Não há benchmark nesta análise. | Medir criação, consulta e listagem com volumes representativos. | Os ganhos descritos são estruturais; nenhum percentual de aceleração foi medido. |

## 05 Trechos a transformar em funções

| Função sugerida | Responsabilidade | Onde aplicar |
|---|---|---|
| ler_inteiro(mensagem, minimo, maximo=None) | Repetir entrada até receber um inteiro no intervalo. | Menu, quantidade de itens, seleção e estoque. |
| ler_valor_monetario(mensagem) | Converter preço, rejeitar não finitos e aplicar a regra de valor. | Cadastro de produto. |
| ler_texto_obrigatorio(mensagem) | Remover espaços e rejeitar texto vazio. | Nome do cliente e do produto. |
| confirmar(mensagem) | Validar S/N e retornar booleano. | Confirmação de alteração de status. |
| gerar_numero_pedido(numeros_usados) | Criar número único e detectar esgotamento. | Início da criação do pedido. |
| selecionar_produto(catalogo) | Exibir opções, validar seleção e permitir voltar. | Inclusão de produtos no pedido. |
| solicitar_pedido(lista_pedidos) | Coletar número, reutilizar busca e tratar ausência ou cancelamento. | Consulta e alteração de status. |
| montar_pedido(numero, cliente, itens) | Retornar o pedido sem teclado, impressão ou alteração de listas externas. | Criação do pedido. |
| definir_status(pedido, novo_status) | Validar o status permitido e aplicar a mudança. | Alteração de status. |
| carregar_dados(caminho) / salvar_dados(caminho, dados) | Concentrar persistência e tratamento de erros de arquivo. | Inicialização e confirmação das alterações. |
| Critério de organização | Agrupar funções relacionadas; validar regras também fora da interface. | Não é necessário criar um arquivo para cada função. |

## 06 Interface Rich com tema Dracula

| Elemento | Aplicação |
|---|---|
| Cabeçalho | Identidade da Bueno’s Store, quantidade de pedidos e pendências. |
| Tabela de pedidos | Número, cliente, produtos e status com cor e texto. |
| Consulta | Detalhes em painel; número zero permite voltar; ausência gera mensagem. |
| Alteração de status | Lista de estados disponíveis e confirmação antes da mudança. |
| Limites do exemplo | Dados fictícios em memória. Não cadastra produtos ou pedidos, calcula total ou salva alterações. |
| Dados com colchetes | Nomes e produtos são renderizados como Text para não interpretar formatação. |
| Imagem da interface | Gerada a partir da saída real do Rich. A imagem abaixo é estática; a interação acontece no script Python. |
| Compatibilidade de cores | A prévia usa a paleta Dracula. O terminal pode adaptar cores conforme seu suporte e suas configurações. |

![Interface Rich com tema Dracula](interface_dracula.png)


## 07 Paleta visual

| Cor | Código | Uso |
|---|---|---|
| Fundo | #282A36 | Base escura da interface e da documentação. |
| Superfície | #343746 | Alternância das linhas para facilitar a leitura. |
| Texto | #F8F8F2 | Conteúdo principal com alto contraste. |
| Roxo | #BD93F9 | Bordas, cabeçalhos e organização visual. |
| Rosa | #FF79C6 | Identidade e destaque do status Enviado. |
| Ciano | #8BE9FD | Informações e status Preparando. |
| Verde | #50FA7B | Pontos positivos e status Entregue. |
| Amarelo | #F1FA8C | Avisos e status Pendente. |

## 08 Como executar

| Etapa | Comando ou orientação |
|---|---|
| Preparar | Abrir o terminal na pasta que contém exemplo_rich.py. Python deve estar instalado e disponível no terminal. |
| Instalar a dependência | python -m pip install -r requirements-demo.txt |
| Abrir a demonstração | python exemplo_rich.py |
| Mostrar apenas a prévia | python exemplo_rich.py --preview |
| Encerrar | Escolher 4 no menu, pressionar Ctrl+C ou encerrar a entrada. |

## 09 Validação e plano de evolução

| Etapa | Resultado ou próxima ação |
|---|---|
| Problemas reproduzidos | TypeError ao alterar pedido inexistente; cadastro aceitou estoque -3 e preço -2.0; catálogo vazio repetiu seleção sem saída válida. |
| Demonstração verificada | Prévia, consulta, pedido inexistente, entrada inválida, cancelamento, atualização de status, saída, lista vazia e texto literal. |
| Passo 1 | Corrigir catálogo vazio, pedido inexistente e validações numéricas. |
| Passo 2 | Extrair entradas repetidas e separar a construção do pedido da interação. |
| Passo 3 | Adicionar quantidade, preço da compra, total e controle de estoque. |
| Passo 4 | Implementar persistência e testes das regras. |
| Passo 5 | Integrar a interface Rich ao fluxo principal e atualizar a documentação. |
| Passo 6 | Medir com mais dados antes de adotar índices e outro armazenamento. |
