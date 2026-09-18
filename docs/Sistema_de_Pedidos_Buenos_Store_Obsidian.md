---
linguagem: Python
projeto: Sistema de Pedidos --- Bueno's Store
status: em-desenvolvimento
tags:
- python
- projeto
- backend
- estudos
- sistema-de-pedidos
---

# 📦 Sistema de Pedidos --- Bueno's Store

> \[!info\] Visão geral Projeto de estudos em **Python** criado para
> praticar lógica de programação por meio de um sistema de gerenciamento
> de pedidos. O projeto começou pequeno, como exercício de revisão, mas
> cresceu conforme novas necessidades foram surgindo: catálogo de
> produtos, validações, consulta, alteração de status, cadastro de
> clientes, modularização e melhoria da interface.

------------------------------------------------------------------------

## 🎯 Objetivo do projeto

O objetivo principal não é construir um sistema comercial completo, mas
aplicar na prática os conteúdos estudados em Python:

-   funções, parâmetros, argumentos e `return`;
-   listas e dicionários;
-   `for` e `while`;
-   condicionais;
-   `try/except`;
-   validação de entradas;
-   modularização;
-   busca de dados;
-   objetos mutáveis;
-   `.append()`, `.copy()`, `enumerate()` e `.join()`;
-   organização e apresentação de dados no terminal.

O projeto acabou funcionando como uma revisão integrada dos assuntos
estudados.

------------------------------------------------------------------------

# 🕒 Evolução do projeto

## 1. Planejamento inicial

O sistema começou com a definição das informações básicas de um pedido:

-   número do pedido;
-   cliente;
-   produto;
-   quantidade;
-   valor total;
-   status.

Antes da implementação, foi criado um **fluxograma em blocos no
Excalidraw** para visualizar o funcionamento do programa.

O planejamento evoluiu para um menu principal:

``` text
╔══════════════════════════════════════════╗
║     SISTEMA DE PEDIDOS – BUENO'S STORE  ║
╠══════════════════════════════════════════╣
║ [1] Criar pedido                        ║
║ [2] Consultar pedido                    ║
║ [3] Listar pedidos                      ║
║ [4] Sair                                ║
╚══════════════════════════════════════════╝
```

O fluxograma foi dividido em áreas para representar responsabilidades
diferentes, como menu, cadastro e produtos.

------------------------------------------------------------------------

## 2. Estrutura inicial dos dados

As principais estruturas do programa passaram a ser listas de
dicionários:

``` python
lista_pedidos = []
catalogo_produtos = []
```

Cada produto possui informações como:

``` text
Nome
Quantidade em estoque
Valor
Categoria
```

E cada pedido foi evoluindo para uma estrutura semelhante a:

``` python
pedido = {
    "Nº do pedido": 629341,
    "Cliente": "Nome do cliente",
    "CPF": "...",
    "Email": "...",
    "Telefone": "...",
    "Endereço": "...",
    "Cidade": "...",
    "Estado": "...",
    "Lista de produtos": [],
    "Status": "Pendente"
}
```

------------------------------------------------------------------------

# 🛍️ Catálogo de produtos

Foi criada uma área específica para cadastrar e exibir produtos.

## Cadastro

O cadastro trabalha com:

-   nome;
-   quantidade em estoque;
-   valor;
-   categoria.

Foram adicionadas validações para impedir valores inválidos, como
quantidade ou preço menor ou igual a zero.

Durante essa etapa também foi usado:

``` python
produto.copy()
```

para evitar ligações indesejadas entre o dicionário temporário e os
itens armazenados na lista.

## Interface

A exibição do catálogo passou por duas experiências:

1.  apresentação simples com `print()`;
2.  teste com a biblioteca **Rich**, utilizando tabela.

A experiência com Rich também trouxe aprendizado sobre ambiente Python e
imports. Um arquivo local chamado `rich.py` chegou a entrar em conflito
com a biblioteca instalada e precisou ser renomeado.

------------------------------------------------------------------------

# 🧾 Criação de pedidos

A função:

``` python
criar_pedidos(lista_pedidos, catalogo_produtos)
```

ficou responsável pelo fluxo principal de criação.

## Número do pedido

O número é gerado aleatoriamente com **6 dígitos**, dentro do intervalo:

``` text
100000–999999
```

Foi criada uma verificação para evitar números repetidos em
`lista_pedidos`.

## Quantidade de produtos

A quantidade informada pelo usuário é validada com `try/except`.

Regras:

-   precisa ser numérica;
-   precisa ser maior que zero.

## Escolha dos produtos

O catálogo é apresentado e o usuário escolhe produtos por posição.

Foi necessário trabalhar com a diferença entre a posição mostrada ao
usuário e o índice real da lista:

``` python
escolha_user - 1
```

------------------------------------------------------------------------

# 👤 Cadastro do cliente

Com o crescimento do projeto, o cadastro do cliente foi separado em uma
função própria:

``` python
ficha_cliente(pedido)
```

Ela recebe o dicionário `pedido` e adiciona as informações do cliente
diretamente nele.

Dados atuais:

-   nome;
-   CPF;
-   data de nascimento;
-   e-mail;
-   telefone;
-   endereço;
-   cidade;
-   estado.

### Decisão sobre os tipos

CPF, telefone e data são tratados preferencialmente como `str`.

O motivo é que são informações/identificadores, e não quantidades
matemáticas. Isso também permite formatos como:

``` text
CPF:       123.456.789-01
Telefone:  (34) 99984-9343
Data:      17/04/1998
```

Uma melhoria planejada é criar funções específicas para **formatação e
validação** desses campos.

------------------------------------------------------------------------

# 🔎 Busca de pedidos

Durante o desenvolvimento foi percebido que `consultar_pedido()` e
`alterar_status()` repetiam a mesma lógica de busca.

Essa responsabilidade foi separada:

``` python
def buscar_pedidos(consulta, lista_pedidos):

    for n_pedido in lista_pedidos:
        if consulta == n_pedido["Nº do pedido"]:
            return n_pedido

    return None
```

### Fluxo

``` text
Número pesquisado
       ↓
Percorrer lista_pedidos
       ↓
Pedido encontrado?
   ┌───────┴───────┐
  SIM             NÃO
   ↓                ↓
return pedido    return None
```

Essa refatoração foi especialmente importante para praticar **`return`**
e separação de responsabilidades.

------------------------------------------------------------------------

# 🔍 Consulta de pedidos

`consultar_pedido()` ficou responsável por:

1.  solicitar o número;
2.  validar se a entrada pode ser convertida para `int`;
3.  chamar `buscar_pedidos()`;
4.  repetir a consulta caso receba `None`;
5.  encaminhar o pedido encontrado para exibição.

Durante essa implementação ocorreu um loop infinito por causa da
inversão entre:

``` text
continue → próxima repetição do laço
break    → encerra o laço
return   → encerra a função e pode devolver um valor
```

A correção ajudou a consolidar a diferença entre os três comandos.

Também ocorreu:

``` text
TypeError: 'module' object is not callable
```

O erro aconteceu porque o nome utilizado representava o **módulo**
`buscar_pedidos`, e não diretamente a função contida nele. Isso reforçou
a compreensão da relação:

``` text
módulo.função(...)
```

------------------------------------------------------------------------

# 🖥️ Ficha de exibição

A apresentação do pedido também foi separada da busca.

Função:

``` python
mostra_ficha(pedido)
```

Responsabilidade: **somente apresentar um pedido já encontrado**.

Exemplo visual:

``` text
╔══════════════════════════════════════════════════════════╗
║                   DETALHES DO PEDIDO                     ║
╠══════════════════════════════════════════════════════════╣
║  Nº DO PEDIDO: 629341                                    ║
╠══════════════════════════════════════════════════════════╣
║  DADOS DO CLIENTE                                        ║
║                                                          ║
║  Cliente:     Mariana Ferreira Costa                     ║
║  CPF:         529.982.247-25                             ║
║  E-mail:      mariana.costa@example.com                  ║
║  Telefone:    (34) 99123-4567                            ║
║  Cidade:      Uberlândia                                 ║
║  Estado:      MG                                         ║
╠══════════════════════════════════════════════════════════╣
║  PRODUTOS                                                ║
║                                                          ║
║  01. Mochila                                             ║
║  02. Mouse                                               ║
║  03. Teclado                                             ║
╠══════════════════════════════════════════════════════════╣
║  STATUS: Pendente                                        ║
╚══════════════════════════════════════════════════════════╝
```

Os produtos são numerados com `enumerate()`.

Para uma exibição compacta:

``` python
", ".join(pedido["Lista de produtos"])
```

gera:

``` text
Produtos: Mochila, Mouse, Teclado
```

------------------------------------------------------------------------

# 📋 Lista de produtos do pedido

Essa parte passou por uma refatoração importante.

Inicialmente, `"Lista de produtos"` acabava recebendo uma `str`:

``` python
"Lista de produtos": "Mochila"
```

Ao usar `for`, o programa percorria a palavra caractere por caractere:

``` text
01. M
02. o
03. c
04. h
05. i
06. l
07. a
```

A estrutura correta é:

``` python
"Lista de produtos": []
```

e os nomes são acrescentados com:

``` python
pedido["Lista de produtos"].append(...)
```

Resultado:

``` python
["Mochila", "Mouse", "Teclado"]
```

Também foi percebido que uma lista intermediária como
`pedidos_comprados` pode ser redundante caso sirva apenas para depois
transferir os nomes para `"Lista de produtos"`. Nesse caso, o nome pode
ser adicionado diretamente ao pedido no momento da escolha.

------------------------------------------------------------------------

# 🔄 Status do pedido

Os status definidos para o sistema são:

``` text
Pendente
Preparando
Enviado
Entregue
```

A função `alterar_status(lista_pedidos)` busca o pedido pelo número e
permite selecionar um novo estado.

A separação de `buscar_pedidos()` permite reutilizar a mesma busca tanto
na consulta quanto na alteração do status.

------------------------------------------------------------------------

# 📃 Listagem dos pedidos

A função:

``` python
listar(lista_pedidos)
```

percorre todos os pedidos cadastrados e apresenta suas informações.

Também existe tratamento para o caso:

``` text
Nenhum pedido cadastrado.
```

O uso de `enumerate()` permite numerar os pedidos apresentados no
terminal.

------------------------------------------------------------------------

# 🧩 Organização atual das responsabilidades

``` text
MAIN
│
├── lista_pedidos
├── catalogo_produtos
│
└── menu principal
      │
      ├── criar_pedidos()
      │     ├── gera Nº
      │     ├── ficha_cliente()
      │     ├── seleciona produtos
      │     └── salva pedido
      │
      ├── consultar_pedido()
      │     ├── valida Nº
      │     ├── buscar_pedidos()
      │     └── mostra_ficha()
      │
      ├── listar()
      │
      └── alterar_status()
            └── buscar_pedidos()
```

> \[!important\] A direção atual da refatoração é manter cada função com
> uma responsabilidade clara, em vez de concentrar entrada, validação,
> busca, alteração e apresentação no mesmo bloco.

------------------------------------------------------------------------

# 🐛 Principais erros e aprendizados

  -----------------------------------------------------------------------
  Problema                            Aprendizado
  ----------------------------------- -----------------------------------
  `UnboundLocalError` envolvendo      Evitar conflito entre nome de
  `produto`                           módulo e variável local

  `ModuleNotFoundError` / conflito    Arquivos locais podem sombrear
  com Rich                            bibliotecas instaladas

  `'module' object is not callable`   Diferenciar módulo de função

  Loop infinito na consulta           Entender corretamente `continue` e
                                      `break`

  Apenas último produto permanecia    `=` substitui; `.append()` adiciona

  `"Mochila"` aparecia letra por      `str` também é iterável; era
  letra                               necessário armazenar uma lista

  Lista zerada dentro do `for`        Inicializar a lista antes do laço

  Código de busca repetido            Extrair responsabilidade para
                                      função reutilizável

  Funções fazendo tarefas demais      Separar busca, entrada, alteração e
                                      exibição
  -----------------------------------------------------------------------

------------------------------------------------------------------------

# 🧠 Conceitos consolidados/praticados

## Estruturas

-   listas;
-   dicionários;
-   listas de dicionários;
-   objetos mutáveis.

## Controle

-   `if / elif / else`;
-   `for`;
-   `while True`;
-   `break`;
-   `continue`.

## Funções

-   parâmetros;
-   argumentos;
-   passagem de dicionários;
-   `return`;
-   retorno de dicionário;
-   retorno de `None`;
-   responsabilidade de funções;
-   reutilização.

## Validação

-   `try/except ValueError`;
-   conversão para `int` e `float`;
-   verificação de faixa;
-   valores maiores que zero;
-   tratamento de entradas inválidas.

## Manipulação/apresentação

-   `.append()`;
-   `.copy()`;
-   `.join()`;
-   `enumerate()`;
-   alinhamento com f-strings;
-   interfaces ASCII;
-   experiência com Rich.

------------------------------------------------------------------------

# 📈 Evolução da arquitetura

Uma das mudanças mais importantes foi sair de uma lógica concentrada:

``` text
função
├── pede dados
├── valida
├── procura
├── imprime
└── altera
```

para uma estrutura mais modular:

``` text
Entrada
   ↓
Validação
   ↓
Busca
   ↓
Regra do sistema
   ↓
Apresentação
```

O projeto ainda não está finalizado, mas já deixou de ser apenas um
exercício isolado e passou a servir como laboratório para **organização
de código e comunicação entre funções**.

------------------------------------------------------------------------

# 🚧 Próximas melhorias

-   [ ] Padronizar validações que aparecem em mais de uma função.
-   [ ] Criar formatação de CPF.
-   [ ] Criar formatação de telefone.
-   [ ] Validar CPF.
-   [ ] Validar campos vazios do cliente.
-   [ ] Melhorar validação de e-mail/data conforme necessidade do
    projeto.
-   [ ] Revisar a necessidade de `pedidos_comprados`.
-   [ ] Trabalhar quantidade de unidades de cada produto.
-   [ ] Integrar estoque à criação do pedido.
-   [ ] Calcular valor total.
-   [ ] Impedir compra acima do estoque disponível.
-   [ ] Continuar reduzindo responsabilidades duplicadas.
-   [ ] Revisar organização final dos módulos.
-   [ ] Atualizar o fluxograma conforme a implementação final.

------------------------------------------------------------------------

# 💡 Regras e decisões do projeto

> \[!note\] Decisões atuais - Número do pedido: **6 dígitos**. - Número
> deve ser único. - Status inicial: **Pendente**. - Produtos do pedido
> são armazenados em uma **lista**. - A ficha do cliente faz parte do
> pedido. - Busca retorna o **dicionário encontrado** ou `None`. -
> Funções de busca não devem ser responsáveis pela interface. - Dados
> como CPF e telefone devem ser tratados como identificadores/texto, não
> como quantidades.

------------------------------------------------------------------------

# 📝 Registro de desenvolvimento

O projeto começou como um **mini projeto para revisão de Python**, mas
cresceu conforme novas regras e responsabilidades foram adicionadas.

O desenvolvimento envolveu planejamento visual, implementação, testes,
identificação de bugs e refatoração. Vários problemas encontrados
durante o processo foram consequência direta do aumento da complexidade
do sistema --- e serviram como exercícios práticos de lógica, funções e
modularização.

> \[!quote\] **"Era pra ser só um mini projeto de estudos, mas quando
> percebi já estava maior do que eu esperava."**

------------------------------------------------------------------------

## 🔗 Notas relacionadas

Você pode criar futuramente no Obsidian:

``` text
[[Python - Funções]]
[[Python - Dicionários]]
[[Python - Listas]]
[[Python - Tratamento de Erros]]
[[Python - Rich]]
[[Git e GitHub]]
[[Fluxograma - Sistema de Pedidos]]
```
