## Documentação do Desafio Delivery App

O aplicativo de entrega que permite calcular a distância entre dois endereços, registrando a sua consulta em um histórico

### Visão geral

Página inicial (`home.html`): Exibe uma página de boas-vindas ao aplicativo, com opções para acessar as páginas de cliente, entregador e calculadora de distâncias.

Página do cliente e entregador (`cliente.html`, `entregador.html`): Não há informações ou codificação foi apenas criada a interface e sua rota de acesso para completar design.

Calculadora de distâncias (`calculator.html`): Permite aos usuários calcular a distância entre dois endereços. Utiliza a API Nominatim para obter dados de localização com base nos endereços fornecidos e a biblioteca geopy para calcular a distância entre as coordenadas geográficas.

Histórico de consultas (`history.html`): Exibe o histórico das consultas de distâncias realizadas pelos usuários.


### Componentes Principais

- Flask: Framework web em Python
- HTML: Renderização das páginas e exibir conteúdos aos usuários
- CSS: Criação de design
- Bootstrap: Framework front-end trazendo estilos predefinidos e componentes do HTML, facilitando a criação de layouts e estilização de elementos, tornando a aplicação mais atraente
- Geopy: Biblioteca para calcular a distância entre dois endereços com base em suas coordenadas geográficas
- API Nominatim: API de geocodificação e pesquisa de endereços


### Funcionalidades Principais

#### Calculadora de Distâncias

Permite aos usuários calcular a distância de origem e destino. A API Nominatim é utilizada para obter as coordenadas geográficas correspondentes a esses endereços. O Geopy realiza o cálculo entre as coordenadas geográficas e apresenta aos usuários a distância calculada.

#### Histórico de Consultas

O histórico das consultas é realizado e armazenado em uma lista. A página mostra as últimas consultas realizadas.


### Perguntas

1. Diga-nos quais partes de software você acha necessárias para desenvolver o protótipo funcional e como elas estão relacionadas. Chamamos de "peça de software" cada aplicativo (web, móvel ou desktop), cada API e cada processo em lote que pode ser implantado de forma independente. Apoie-se em um diagrama, se achar necessário.

2. Fale sobre o tipo de arquitetura que você escolheu para a pergunta (1). Monolítica? Microsserviços? Algum intermediário? Outro? Comente sobre o que você baseou para tomar essa decisão.

3. Descreva a metodologia de trabalho que você usaria para o desenvolvimento. Pode ser alguma metodologia conhecida (Scrum, XP, RUP), uma adaptação ou uma mistura entre várias metodologias. O que sua experiência mostrou que funciona. Diga-nos por que você acha que essa forma é apropriada para nosso problema.

4. Descreva o fluxo de trabalho que você usaria para colaborar usando o Git. Assim como em (3), você pode usar algo familiar ou fazer uma adaptação.

5. Você acha necessário adicionar algum membro adicional à equipe durante o desenvolvimento do protótipo? Qual seria o seu papel? Você acha necessário adicionar novos membros após a fase do protótipo? Quando e por quê?


### Considerações Finais

Esta documentação abrange os principais aspectos do software "App Delivery". Descreve sua estrutura, funcionalidades, tecnologias utilizadas e integração com a API Nominatim.

O "App Delivery" é uma solução web que simplifica a interação entre clientes e entregadores, fornecendo recursos para cálculo de distâncias entre endereços e facilitando a gestão de tarefas de entrega.

https://bain.nayaraoliveira.repl.co/
