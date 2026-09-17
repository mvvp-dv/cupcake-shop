# Cupcake Shop — PIT II

Primeira versão executável do projeto acadêmico.

## Tecnologias
- HTML
- CSS
- JavaScript
- Python + Flask
- SQLite

## O que já funciona
- Banco SQLite com as 8 tabelas do modelo definido
- Criação automática do banco
- Produtos iniciais cadastrados no banco
- Home/Vitrine responsiva
- Produtos carregados pelo back-end a partir do SQLite
- Botão "Adicionar" com contador temporário de carrinho no front-end

> O carrinho persistente, cadastro/login, checkout, pagamento simulado,
> pedidos, acompanhamento e área administrativa serão implementados nas
> próximas etapas.

## Como executar no Windows

1. Instale Python 3, caso ainda não tenha.
2. Abra o terminal dentro desta pasta.
3. Crie um ambiente virtual:

    python -m venv .venv

4. Ative:

    .venv\Scripts\activate

5. Instale as dependências:

    pip install -r requirements.txt

6. Execute:

    python app.py

7. Abra no navegador:

    http://127.0.0.1:5000

O arquivo `cupcake_shop.db` será criado automaticamente na primeira execução.
