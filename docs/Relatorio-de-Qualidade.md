# Relatório de Qualidade — Cupcake Shop

## Objetivo

Registrar os principais problemas identificados durante o desenvolvimento e a validação da aplicação, bem como as correções realizadas.

| Problema identificado | Correção realizada | Resultado |
|---|---|---|
| O checkout não era carregado corretamente devido ao nome incorreto do arquivo `checkout.htm`. | O arquivo foi renomeado para `checkout.html`, adequando-o à chamada realizada pelo Flask. | Checkout funcionando normalmente. |
| A estilização da aplicação não estava sendo aplicada corretamente em algumas telas. | O arquivo CSS foi revisado e reorganizado para contemplar as telas da aplicação. | Interface apresentada corretamente e de forma responsiva. |
| A área administrativa apresentava produtos e pedidos em uma única página extensa. | A interface administrativa foi reorganizada em seções separadas para “Pedidos” e “Produtos”. | Navegação administrativa mais organizada e funcional. |

## Validação após as correções

Após as correções, o fluxo principal da aplicação foi novamente executado, incluindo cadastro, login, carrinho, checkout, criação de pedido, consulta de pedidos e funcionalidades administrativas.

Posteriormente, a solução foi submetida à validação com cinco usuários. Durante os testes realizados, não foram identificadas novas falhas nas funcionalidades avaliadas.

## Resultado

A versão validada da Cupcake Shop apresentou funcionamento adequado para o escopo definido no projeto.
