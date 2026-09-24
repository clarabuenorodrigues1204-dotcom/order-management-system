# 📦 Order Management System

> ⚠️ **Projeto em desenvolvimento:** este sistema ainda está sendo construído e aprimorado. Algumas funcionalidades podem apresentar bugs, comportamentos inesperados ou sofrer alterações nas próximas versões.

## 📌 Sobre o projeto

O **Order Management System** é um sistema de gerenciamento de pedidos desenvolvido em **Python** com objetivo de praticar e consolidar conceitos de lógica de programação e organização de projetos.

O projeto começou como um exercício de revisão, mas foi evoluindo para um sistema dividido em módulos, com gerenciamento de pedidos, produtos e status.

## 🎯 Objetivos do projeto

Este projeto está sendo desenvolvido principalmente para praticar:

- Funções;
- Parâmetros e argumentos;
- Listas;
- Dicionários;
- Listas de dicionários;
- Estruturas condicionais;
- Laços de repetição;
- Validação de entradas;
- Tratamento de erros;
- Modularização;
- Organização de código.

## ⚙️ Funcionalidades

Atualmente, o sistema permite:

- Criar pedidos;
- Consultar um pedido pelo número;
- Listar pedidos cadastrados;
- Alterar o status de um pedido;
- Cadastrar produtos;
- Exibir o catálogo de produtos;
- Validar diferentes entradas fornecidas pelo usuário.

## 📋 Estrutura dos pedidos

Cada pedido possui informações como:

- **Número do pedido**
- **Cliente**
- **Lista de produtos**
- **Status**

O número do pedido é gerado automaticamente com **6 dígitos**.

### Status disponíveis

Os pedidos podem possuir os seguintes status:

- `Pendente`
- `Preparando`
- `Enviado`
- `Entregue`

## 🛒 Estrutura dos produtos

Os produtos armazenam informações como:

- Nome;
- Categoria;
- Quantidade em estoque;
- Valor.

## 🗂️ Estrutura do projeto

```text
order-management-system/
│
├── main.py
├── menu.py
├── pedidos.py
├── produto.py
└── README.md
```

### `main.py`

Responsável por iniciar a execução do sistema e integrar os diferentes módulos.

### `menu.py`

Responsável pela interface e pelas opções disponíveis no menu principal.

### `pedidos.py`

Contém as principais funcionalidades relacionadas ao gerenciamento dos pedidos.

### `produto.py`

Contém as funcionalidades relacionadas ao cadastro e exibição dos produtos.

## 🖥️ Menu principal

O sistema possui atualmente as seguintes opções:

```text
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

║  Escolha uma opção: 
```

Outras funcionalidades do sistema, como alteração de status e gerenciamento de produtos, continuam sendo desenvolvidas e integradas.

## 🛠️ Tecnologias utilizadas

- **Python**
- **Git**
- **GitHub**

## ▶️ Como executar

Primeiro, clone o repositório:

```bash
git clone URL_DO_REPOSITORIO
```

Entre na pasta do projeto:

```bash
cd order-management-system
```

Depois execute:

```bash
python main.py
```

## 🚧 Próximas melhorias

Algumas melhorias planejadas para o projeto incluem:

- Melhorar e padronizar as validações;
- Aprimorar o tratamento de erros;
- Melhorar a organização dos módulos;
- Corrigir bugs encontrados durante os testes;
- Melhorar a interface do terminal;
- Aprimorar o gerenciamento de produtos;
- Evoluir o controle dos pedidos;
- Refatorar partes do código conforme novos conceitos forem aprendidos;
- Avaliar futuramente o uso de bibliotecas para melhorar a interface do terminal.

## 📚 Contexto

Este projeto faz parte do meu processo de aprendizado em programação e desenvolvimento backend.

Ele está sendo utilizado para colocar em prática conceitos estudados individualmente e entender melhor como diferentes partes de um programa podem trabalhar juntas em um projeto maior.

Por estar em desenvolvimento, a estrutura e as funcionalidades ainda podem mudar ao longo do tempo.

---

### 👩‍💻 Desenvolvido por Clara Bueno

Projeto criado para estudo e prática de **Python, lógica de programação e desenvolvimento backend**.