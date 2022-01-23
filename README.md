# deloitte_challenge

Projeto desenvolvido para o desafio da Gama Academy no processo seletivo da Deloitte.

## Tecnologias utilizadas

O código foi desenvolvido em python 3, foram utilizados o framework flask e algumas libs de extensão como Flask-SQLAlchemy e SQLAlchemy_utils. Para testar a aplicação foi utilizado Postman.

### Flask

O flask é um microframework web escrito em python. Ele é indepente de outras bibliotecas e frameworks, portanto, é amigavel para iniciantes sendo possivel escrever de forma simples e flexivel os serviços para a API CRUD RESTful.

### SQLAlchemy

O Flask-SQLAlchemy foi a biblioteca utilizada para lidar com o banco de dados relacional.

## Estrutura do projeto

O projeto é formado pelo arquivos:

* settings.py: arquivo responsavel pro configurar a aplicação flask.
* api_db.py: arquivo contendo as classes e metodos utilizados para manipular o banco de dados.
* api.py: arquivo contendo a aplicação com seus endpoints.
* database.db: arquivo contendo o banco de dados relacional.

### settings.py

Importa o framework e as bibliotecas utilizadas, cria objeto da aplicação e o configura.

### api_db.py

Cria as classes e metodos para lidar com as tabelas do banco de dados: tabela de membros da equipe, tabela de serviços e tabela de posts.
Verifica se o banco de dados já foi criado, caso contrario o cria incluindo alguns dados para testes.

### api.py

Apresenta todos os endpoints da aplicação e configura a porta utilizada para executar a aplicação.
