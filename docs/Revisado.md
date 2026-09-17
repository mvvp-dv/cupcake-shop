# Documentação Revisada

## Cupcake Shop

### 1. Visão do projeto

A Cupcake Shop é uma aplicação web desenvolvida para apoiar a venda de cupcakes pela internet.

A solução permite que o cliente visualize os produtos disponíveis, realize seu cadastro, faça login, adicione produtos ao carrinho, informe o endereço de entrega, escolha uma forma de pagamento e acompanhe o andamento do pedido.

Também foi desenvolvida uma área administrativa para gerenciamento dos produtos e atualização do status dos pedidos.

---

## 2. Objetivo

Desenvolver uma aplicação web simples e responsiva que digitalize o processo de venda de cupcakes, contemplando as etapas de vitrine, pedido eletrônico, pagamento demonstrativo e acompanhamento da entrega.

---

## 3. Escopo da solução

### Cliente

O cliente pode:

- visualizar os cupcakes disponíveis;
- criar uma conta;
- realizar login;
- adicionar produtos ao carrinho;
- aumentar ou diminuir quantidades;
- remover produtos;
- visualizar o valor total;
- informar o endereço de entrega;
- escolher a forma de pagamento;
- confirmar o pedido;
- consultar seus pedidos;
- acompanhar o status do pedido.

### Administrador

O administrador pode:

- acessar uma área administrativa;
- cadastrar novos cupcakes;
- editar produtos existentes;
- alterar preço e descrição;
- definir a disponibilidade dos produtos;
- consultar os pedidos realizados;
- atualizar o status dos pedidos.

---

# 4. Histórias de Usuário

## US01 — Visualizar produtos

**Solicitante:** Cliente  
**Ação:** Visualizar os cupcakes disponíveis na vitrine virtual.  
**Critério de aceitação:** A aplicação deve apresentar nome, descrição, preço e representação visual do produto.  
**Prioridade:** A  
**Story Points:** 3

---

## US02 — Visualizar informações do produto

**Solicitante:** Cliente  
**Ação:** Consultar as informações necessárias para escolher um cupcake.  
**Critério de aceitação:** Nome, descrição, preço e disponibilidade devem estar visíveis na vitrine.  
**Prioridade:** B  
**Story Points:** 2

---

## US03 — Criar conta

**Solicitante:** Cliente  
**Ação:** Realizar cadastro no sistema.  
**Critério de aceitação:** O sistema deve permitir cadastro com nome, e-mail e senha e impedir a duplicidade de e-mail.  
**Prioridade:** A  
**Story Points:** 3

---

## US04 — Realizar login

**Solicitante:** Cliente  
**Ação:** Entrar na aplicação utilizando e-mail e senha.  
**Critério de aceitação:** Somente usuários com credenciais válidas devem acessar sua conta.  
**Prioridade:** A  
**Story Points:** 3

---

## US05 — Adicionar produto ao carrinho

**Solicitante:** Cliente  
**Ação:** Adicionar um cupcake ao carrinho.  
**Critério de aceitação:** O produto selecionado deve ser registrado no carrinho do usuário.  
**Prioridade:** A  
**Story Points:** 3

---

## US06 — Visualizar carrinho

**Solicitante:** Cliente  
**Ação:** Consultar os produtos selecionados.  
**Critério de aceitação:** O carrinho deve apresentar produtos, quantidades, subtotais e total do pedido.  
**Prioridade:** A  
**Story Points:** 3

---

## US07 — Alterar quantidade

**Solicitante:** Cliente  
**Ação:** Aumentar ou diminuir a quantidade de um produto.  
**Critério de aceitação:** O sistema deve recalcular os valores após a alteração.  
**Prioridade:** B  
**Story Points:** 2

---

## US08 — Remover produto

**Solicitante:** Cliente  
**Ação:** Remover um produto do carrinho.  
**Critério de aceitação:** O item deve ser excluído e o total recalculado.  
**Prioridade:** B  
**Story Points:** 2

---

## US09 — Informar endereço

**Solicitante:** Cliente  
**Ação:** Informar o endereço para entrega.  
**Critério de aceitação:** Os dados obrigatórios do endereço devem ser preenchidos antes da confirmação do pedido.  
**Prioridade:** A  
**Story Points:** 3

---

## US10 — Escolher pagamento

**Solicitante:** Cliente  
**Ação:** Selecionar a forma de pagamento.  
**Critério de aceitação:** O sistema deve disponibilizar Pix, cartão de crédito e cartão de débito.

**Regra de negócio:** O pagamento é demonstrativo para fins acadêmicos e não realiza transação financeira real.  
**Prioridade:** A  
**Story Points:** 3

---

## US11 — Confirmar pedido

**Solicitante:** Cliente  
**Ação:** Revisar e confirmar a compra.  
**Critério de aceitação:** O sistema deve registrar produtos, endereço, valor e forma de pagamento.  
**Prioridade:** A  
**Story Points:** 3

---

## US12 — Receber número do pedido

**Solicitante:** Cliente  
**Ação:** Receber a confirmação da realização do pedido.  
**Critério de aceitação:** Após a confirmação, o sistema deve gerar um identificador para o pedido.  
**Prioridade:** A  
**Story Points:** 2

---

## US13 — Consultar e acompanhar pedidos

**Solicitante:** Cliente  
**Ação:** Consultar os pedidos realizados e seu andamento.  
**Critério de aceitação:** O sistema deve apresentar o pedido e seu status atual.

**Status previstos:**

1. Recebido
2. Em preparo
3. Saiu para entrega
4. Entregue

Quando o pedido estiver como "Saiu para entrega", a aplicação apresenta uma representação visual demonstrativa da rota.

**Prioridade:** B  
**Story Points:** 3

---

## US14 — Gerenciar produtos

**Solicitante:** Administrador  
**Ação:** Cadastrar e editar cupcakes.  
**Critério de aceitação:** O administrador deve conseguir alterar nome, descrição, preço, imagem e disponibilidade.  
**Prioridade:** B  
**Story Points:** 5

---

## US15 — Gerenciar pedidos

**Solicitante:** Administrador  
**Ação:** Consultar pedidos e atualizar seus status.  
**Critério de aceitação:** A alteração realizada pelo administrador deve ficar registrada e ser apresentada posteriormente ao cliente.  
**Prioridade:** B  
**Story Points:** 5

---

# 5. Casos de Uso

Os principais casos de uso identificados são:

**UC01 — Realizar cadastro**  
Ator: Cliente

**UC02 — Realizar login**  
Ator: Cliente

**UC03 — Gerenciar carrinho**  
Ator: Cliente

**UC04 — Realizar pedido**  
Ator: Cliente

**UC05 — Consultar e acompanhar pedido**  
Ator: Cliente

**UC06 — Gerenciar produtos**  
Ator: Administrador

**UC07 — Gerenciar pedidos**  
Ator: Administrador

---

# 6. Diagrama Geral de Casos de Uso

```mermaid
flowchart LR

Cliente((Cliente))
Admin((Administrador))

UC01[Realizar cadastro]
UC02[Realizar login]
UC03[Gerenciar carrinho]
UC04[Realizar pedido]
UC05[Consultar e acompanhar pedido]

UC06[Gerenciar produtos]
UC07[Gerenciar pedidos]

Cliente --> UC01
Cliente --> UC02
Cliente --> UC03
Cliente --> UC04
Cliente --> UC05

Admin --> UC02
Admin --> UC06
Admin --> UC07
```
---

# 7. Diagrama de Classes

O diagrama de classes representa as principais entidades da aplicação e os relacionamentos existentes entre elas.

```mermaid
classDiagram
direction TB

class Usuario {
    +int id
    +string nome
    +string email
    +string senha_hash
    +string tipo
}

class Endereco {
    +int id
    +int usuario_id
    +string rua
    +string numero
    +string bairro
    +string cidade
    +string cep
}

class Produto {
    +int id
    +string nome
    +string descricao
    +float preco
    +boolean disponivel
}

class Carrinho {
    +int id
    +int usuario_id
}

class ItemCarrinho {
    +int id
    +int carrinho_id
    +int produto_id
    +int quantidade
}

class Pedido {
    +int id
    +int usuario_id
    +int endereco_id
    +float valor_total
    +string status
}

class ItemPedido {
    +int id
    +int pedido_id
    +int produto_id
    +int quantidade
    +float preco_unitario
}

class Pagamento {
    +int id
    +int pedido_id
    +string forma
    +string status
}

Usuario --> Endereco
Usuario --> Carrinho
Usuario --> Pedido
Carrinho --> ItemCarrinho
ItemCarrinho --> Produto
Pedido --> ItemPedido
ItemPedido --> Produto
Pedido --> Pagamento
Pedido --> Endereco
```
---

# 8. Diagrama de Sequência

O diagrama de sequência representa o fluxo principal para realização de um pedido na aplicação.

```mermaid
sequenceDiagram
    actor Cliente
    participant Interface
    participant Backend
    participant Banco

    Cliente->>Interface: Visualiza os cupcakes
    Interface->>Backend: Solicita produtos
    Backend->>Banco: Consulta produtos disponíveis
    Banco-->>Backend: Retorna produtos
    Backend-->>Interface: Exibe vitrine

    Cliente->>Interface: Adiciona produto ao carrinho
    Interface->>Backend: Envia produto e quantidade
    Backend->>Banco: Registra item no carrinho

    Cliente->>Interface: Continua o pedido
    Interface->>Cliente: Solicita endereço e pagamento
    Cliente->>Interface: Informa os dados
    Interface->>Backend: Confirma pedido
    Backend->>Banco: Registra endereço
    Backend->>Banco: Registra pedido e itens
    Backend->>Banco: Registra pagamento demonstrativo
    Banco-->>Backend: Retorna número do pedido
    Backend-->>Interface: Confirma realização do pedido
    Interface-->>Cliente: Exibe pedido e status
```
---

# 9. Modelo do Banco de Dados

A aplicação utiliza SQLite para persistência dos dados. O modelo é composto por oito tabelas responsáveis pelo cadastro dos usuários, produtos, carrinho, pedidos, endereços e pagamentos.

```mermaid
erDiagram
    USUARIOS ||--o{ ENDERECOS : possui
    USUARIOS ||--|| CARRINHOS : possui
    USUARIOS ||--o{ PEDIDOS : realiza

    CARRINHOS ||--o{ ITENS_CARRINHO : contem
    PRODUTOS ||--o{ ITENS_CARRINHO : compoe

    PEDIDOS ||--|{ ITENS_PEDIDO : contem
    PRODUTOS ||--o{ ITENS_PEDIDO : compoe

    PEDIDOS ||--|| PAGAMENTOS : possui
    ENDERECOS ||--o{ PEDIDOS : utilizado_em

    USUARIOS {
        int id PK
        string nome
        string email
        string senha_hash
        string tipo
    }

    ENDERECOS {
        int id PK
        int usuario_id FK
        string rua
        string numero
        string complemento
        string bairro
        string cidade
        string cep
    }

    PRODUTOS {
        int id PK
        string nome
        string descricao
        float preco
        string imagem
        boolean disponivel
    }

    CARRINHOS {
        int id PK
        int usuario_id FK
    }

    ITENS_CARRINHO {
        int id PK
        int carrinho_id FK
        int produto_id FK
        int quantidade
    }

    PEDIDOS {
        int id PK
        int usuario_id FK
        int endereco_id FK
        datetime data
        float valor_total
        string status
    }

    ITENS_PEDIDO {
        int id PK
        int pedido_id FK
        int produto_id FK
        int quantidade
        float preco_unitario
    }

    PAGAMENTOS {
        int id PK
        int pedido_id FK
        string forma
        string status
    }
```
