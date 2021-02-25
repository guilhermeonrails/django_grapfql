### Introdução

- O que é uma API REST?
- O que é grapqhl? 
- Qual a diferença entre uma API REST e uma API com Grapqhl?
- Qual o benefício de utilizar graphql ao invés de Rest?
- Como usar o graphql no python? Qual biblioteca que permite fazer essa integração?
- Colocar gif do site do graphql de uma consulta graphql
- Mostrar um exemplo de API do Django Rest Framework

### Hello World com Graphql

- Criar a venv
- Instalar o django
- Criar um projeto django chamado "setup"
  - ```django-admin startproject setup .```
- Ir ao arquivo ```settings.py``` e colocar a linguagem para pt-br e alterar o time_zone:
  - ```LANGUAGE_CODE = 'pt-br'```
  - ```TIME_ZONE = 'America/Sao_Paulo'```
- Com o projeto configurado, podemos instalar a biblioteca graphene para trabalharmos com o graphql:
  - ```pip install graphene-django```
- Adicione graphene_django ao INSTALLED_APPS no settings.py:
    ```
        INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'graphene_django'
        ]
    ```
- Adiicionar uma url para consultar a API graphql
  - Teremos apenas uma URL, pois toda consulta será feito por meio da interface do graphql por meio dessa URL
  - Importar o GraphqlView:
    - ```from graphene_django.views import GraphQLView```
    - Após isso, adicionar a url path:
    - ```path("graphql", GraphQLView.as_view(graphiql=True))```
      - Mude graphiql=True para graphiql=False se não quiser usar o navegador GraphiQL API.
      - Mas o que é esse GraphiQL? GraphiQL - é um IDE integrado para executar suas consultas!
      - GraphiQL é muito útil durante o desenvolvimento, mas é prática padrão desabilitar essa visualização na produção, pois pode permitir que um desenvolvedor externo tenha muitos insights sobre a API, por causa da documentação que ele mostra. Então em produção é interessante desativar esse visualizador colocando graphiql=False
      - Ler esse artigo sobre comunicação via POST
        - https://stackabuse.com/building-a-graphql-api-with-django/
      - COMO CHAMAR UMA API GRAPHQL DO LADO FRONTEND? https://www.apollographql.com/blog/4-simple-ways-to-call-a-graphql-api-a6807bcdb355/
      - 
  - Colocar em settings.py a configuração de onde está localizado o schema graphql, ou seja, os recursos da nossa API, quais os dados iremos ter na API.
    - ```GRAPHENE = {
    "SCHEMA": "setup.schema.schema"
    }```
    - Criar o arquivo schema.py
    - 
    ```
        import graphene
        class Query(graphene.ObjectType):
            hello = graphene.String(default_value="Hi")

        schema = graphene.Schema(query=Query)
        ```
    - Executar o servidor na rota /graphql e digitar:
    - ```
        query {
            hello
        }
        ou simplesmente:
        {
  	        hello
        }
        ```
        ![image](https://user-images.githubusercontent.com/41811634/108797093-281df580-7569-11eb-8198-f24ecaa80958.png)
    - A palavra "query" é opcional e as chaves demarcam o início de uma consulta graphql
    - https://www.howtographql.com/basics/2-core-concepts/
    - https://docs.graphene-python.org/projects/django/en/latest/installation/