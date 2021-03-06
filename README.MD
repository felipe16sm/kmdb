# Comandos SQL

# Dropar todas as tabelas

drop owned by root;

# Criar Banco de dados:

CREATE DATABASE db;

# Criar Usuário:

CREATE USER root WITH ENCRYPTED PASSWORD 'root';

GRANT ALL PRIVILEGES ON DATABASE db TO root;

ALTER USER root CREATEDB;

# Conectar em um Banco de Dados

\c nome_DB

# Installs Django

pip install --upgrade pip && pip install ipdb && pip install django && pip install djangorestframework && pip install markdown && pip install django-filter && pip install psycopg2

# Comandos Django

django-admin startproject nome_projeto .

python manage.py startapp nome_app

python manage.py makemigrations nome_app

python manage.py migrate

python manage.py runserver

TEST=TEST python manage.py test -v 2 &> report.txt

# Rotes

# POST /accounts/ - Create new users.

# Create a user

```sh
// REQUEST


{
    "username": "user",
    "password": "1234",
    "first_name": "John",
    "last_name": "Wick",
    "is_superuser": false,
    "is_staff": false
}
```

```sh
// RESPONSE STATUS -> HTTP 201 CREATED

{
    "id": 1,
    "username": "user",
    "first_name": "John",
    "last_name": "Wick",
    "is_superuser": false,
    "is_staff": false,
}
```

# Create a critic

```sh
// REQUEST

{
    "username": "critic",
    "password": "1234",
    "first_name": "Jacques",
    "last_name": "Aumont",
    "is_superuser": false,
    "is_staff": true
}
```

```sh
// RESPONSE STATUS -> HTTP 201 CREATED

{
    "id": 2,
    "username": "critic",
    "first_name": "Jacques",
    "last_name": "Aumont",
    "is_superuser": false,
    "is_staff": true,
}
```

# Create a administrator

```sh
// REQUEST

{
    "username": "admin",
    "password": "1234",
    "first_name": "Jeff",
    "last_name": "Bezos",
    "is_superuser": true,
    "is_staff": true
}
```

```sh
// RESPONSE STATUS -> HTTP 201 CREATED

{
    "id": 3,
    "username": "admin",
    "first_name": "Jeff",
    "last_name": "Bezos",
    "is_superuser": true,
    "is_staff": true,
}
```

######

# POST /login/ - Login route (must return token)

```sh
// REQUEST

{
    "username": "critic",
    "password": "1234"
}
```

```sh
// RESPONSE STATUS -> HTTP 200 OK


{
    "token": "dfd384673e9127213de6116ca33257ce4aa203cf"
}
```

######

# POST /movies/ - Create a new movie

```sh
// REQUEST

// Header -> Authorization: Token <token-do-admin>

{
    "title": "O Poderoso Chefão",
    "duration": "175m",
    "genres": [
        {"name": "Crime"},
        {"name": "Drama"}
    ],
    "launch": "1972-09-10",
    "classification": 14,
    "synopsis": "Don Vito Corleone (Marlon Brando) é o chefe de uma 'família' de Nova York que está feliz, pois Connie (Talia Shire), sua filha,se casou com Carlo (Gianni Russo). Por ser seu padrinho Vito foi procurar o líder da banda e ofereceu 10 mil dólares para deixar Johnny sair, mas teve o pedido recusado."
}
```

```sh
// RESPONSE STATUS -> HTTP 201 CREATED

{
    "id": 1,
    "title": "O Poderoso Chefão",
    "duration": "175m",
    "genres": [
        {
            "id": 1,
            "name": "Crime"
        },
        {
            "id": 2,
            "name": "Drama"
        }
    ],
    "launch": "1972-09-10",
    "classification": 14,
    "synopsis": "Don Vito Corleone (Marlon Brando) é o chefe de uma 'família' de Nova York que está feliz, pois Connie (Talia Shire), sua filha,se casou com Carlo (Gianni Russo). Por ser seu padrinho Vito foi procurar o líder da banda e ofereceu 10 mil dólares para deixar Johnny sair, mas teve o pedido recusado.",
    "criticism_set": [],
    "comment_set": []
}
```

# GET /movies/ - List all registered movies

```sh
// RESPONSE STATUS 200 OK

[
    {
        "id": 1,
        "title": "O Poderoso Chefão",
        "duration": "175m",
        "genres": [
            {
                "id": 1,
                "name": "Crime"
            },
            {
                "id": 2,
                "name": "Drama"
            }
        ],
        "launch": "1972-09-10",
        "classification": 14,
        "synopsis": "Don Vito Corleone (Marlon Brando) é o chefe de uma 'família' de Nova York que está feliz, pois Connie (Talia Shire), sua filha,se casou com Carlo (Gianni Russo). Por ser seu padrinho Vito foi procurar o líder da banda e ofereceu 10 mil dólares para deixar Johnny sair, mas teve o pedido recusado.",
        "criticism_set": [],
        "comment_set": []
    },
    {
        "id": 2,
        "title": "Um Sonho de Liberdade",
        "duration": "142m",
        "genres": [
            {
                "id": 2,
                "name": "Drama"
            },
            {
                "id": 3,
                "name": "Ficção científica"
            }
        ],
        "launch": "1994-10-14",
        "classification": 16,
        "synopsis": "Andy Dufresne é condenado a duas prisões perpétuas consecutivas pelas mortes de sua esposa e de seu amante. Porém, só Andy sabe que ele não cometeu os crimes. No presídio, durante dezenove anos, ele faz amizade com Red, sofre as brutalidades da vida na cadeia, se adapta, ajuda os carcereiros, etc."
        "criticism_set": [],
        "comment_set": []
    }
]
```

# GET /movies/ - List all movies according to a filter in request

```sh
// REQUEST


{
    "title": "liberdade" // Campo obrigatório
}
```

```sh
// RESPONSE STATUS 200 OK


[
    {
        "id": 2,
        "title": "Um Sonho de Liberdade",
        "duration": "142m",
        "genres": [
            {
                "id": 2,
                "name": "Drama"
            },
            {
                "id": 3,
                "name": "Ficção científica"
            }
    ],
    "launch": "1994-10-14",
    "classification": 16,
    "synopsis": "Andy Dufresne é condenado a duas prisões perpétuas consecutivas pelas mortes de sua esposa e de seu amante. Porém, só Andy sabe que ele não cometeu os crimes. No presídio, durante dezenove anos, ele faz amizade com Red, sofre as brutalidades da vida na cadeia, se adapta, ajuda os carcereiros",
    "criticism_set": [],
    "comment_set": []
    },
    {
        "id": 3,
        "title": "Em busca da liberdade",
        "duration": "175m",
        "genres": [
            {
                "id": 2,
                "name": "Drama"
            },
            {
                "id": 4,
                "name": "Obra de época"
            }
        ],
        "launch": "2018-02-22",
        "classification": 14,
        "synopsis": "Representando a Grã-Bretanha, corredor Eric Liddell (Joseph Fiennes) ganha uma medalha de ouro nas Olimpíadas de Paris em 1924. Ele decide ir até a China para trabalhar como missionário e acaba encontrando um país em guerra. Com a invasão japonesa no território chinês durante a Segunda Guerra Mundial, Liddell acaba em um campo de concentração.",
        "criticism_set": [],
        "comment_set": []
    }
]
```

# GET /movies/<int: movie_id>/ - Search a movie using movie id

```sh
// RESPONSE STATUS -> HTTP 200 OK

{
    "id": 9,
    "title": "Nomadland",
    "duration": "110m",
    "genres": [
        {
            "id": 2,
            "name": "Drama"
        },
        {
            "id": 4,
            "name": "Obra de época"
        }
    ],
    "launch": "2021-04-15",
    "classification": 14,
    "synopsis": "Uma mulher na casa dos 60 anos que, depois de perder tudo na Grande
    Recessão, embarca em uma viagem pelo Oeste americano, vivendo como uma nômade
    moderna.",
    "criticism_set": [
        {
            "id": 39,
            "critic": {
                "id": 2,
                "first_name": "Jacques",
                "last_name": "Aumont",
            },
            "stars": 8,
            "review": "Nomadland apresenta, portanto, fortes credenciais para ser favorito ao Oscar 2021 e Chloé Zhao tem a chance de fazer história como a segunda mulher (apenas) a vencer o maior prêmio do cinema como diretora. Filme com cara de premiação, mas, ainda assim, com mensagens importantes para todos.",
            "spoilers": false
        },
    ...
    ],
    "comment_set": [
        {
            "id": 11,
            "user": {
                "id": 1,
                "first_name": "John",
                "last_name": "Wick"
            },
            "comment": "Lindo, nos faz refletir sobre a vida, os anos, envelhecer. Vale a pena assistir"
        },
    ...
    ]
```

# DELETE /movies/<int:movie_id>/ - Delete movie

# // Response

# 204 No Content

######

# POST /movies/<int:movie_id>/review/ - Create a critic review

```sh
// REQUEST

// Header -> Authorization: Token <token-de-critic>

{
    "stars": 7,
    "review": "Nomadland podia ter dado muito errado. Podia ser dramático demais, monótono demais ou opaco demais. Felizmente, o que vemos é algo singelo, pois a direção de Zhao (que também edita, assina e produz o longa) não ignora a frieza da realidade, mas sabe encontrar a magia da naturalidade. Sim, rimei sem querer e parece meio poético, mas é assim que o filme funciona mesmo. Viva Chloé Zhao - para sempre! Logo, os holofotes voltaram para esta obra independente da cineasta que, sinceramente, merece toda a atenção que recebeu.",
    "spoiler": false,
}
```

```sh
// RESPONSE STATUS 201 CREATED


{
    "id": 39,
    "critic": {
        "id": 2,
        "first_name": "Jacques",
        "last_name": "Aumont"
    },
    "stars": 7,
    "review": "Nomadland podia ter dado muito errado. Podia ser dramático demais, monótono demais ou opaco demais. Felizmente, o que vemos é algo singelo, pois a direção de Zhao (que também edita, assina e produz o longa) não ignora a frieza da realidade, mas sabe encontrar a magia da naturalidade. Sim, rimei sem querer e parece meio poético, mas é assim que o filme funciona mesmo. Viva Chloé Zhao - para sempre! Logo, os holofotes voltaram para esta obra independente da cineasta que, sinceramente, merece toda a atenção que recebeu.",
    "spoilers": false
}
```

# PUT /movies/<int:movie_id>/review/ - Update a critic

```sh
// REQUEST

// Header -> Authorization: Token <token-do-critic>

// All fields are required

{
    "stars": 8,
    "review": "Nomadland apresenta, portanto, fortes credenciais para ser favorito ao Oscar 2021 e Chloé Zhao tem a chance de fazer história como a segunda mulher (apenas) a vencer o maior prêmio do cinema como diretora. Filme com cara de premiação, mas, ainda assim, com mensagens importantes para todos.",
    "spoilers": false
}
```

```sh
//RESPONSE

{
    "id": 39,
    "critic": {
        "id": 2,
        "first_name": "Jacques",
        "last_name": "Aumont"
    },
    "stars": 8,
    "review": "Nomadland apresenta, portanto, fortes credenciais para ser favorito ao Oscar 2021 e Chloé Zhao tem a chance de fazer história como a segunda mulher (apenas) a vencer o maior prêmio do cinema como diretora. Filme com cara de premiação, mas, ainda assim, com mensagens importantes para todos.",
    "spoilers": false
}
```

######

# POST /movies/<int:movie_id>/comments/ - User comment

```sh
// REQUEST

// Header -> Authorization: Token <token-do-user>


{
    "comment": "Lindo filme. Com certeza assistam.",
}
```

```sh
// RESPONSE STATUS -> HTTP 201 CREATED

{
    "id": 1,
    "user": {
        "id": 1,
        "first_name": "John",
        "last_name": "Wick"
    },
    "comment": "Lindo filme. Com certeza assistam."
}
```

# PUT /movies/<int:movie_id>/comments/ - Update an user comment

```sh
// REQUEST

// Header -> Authorization: Token <token-do-user>

{
    "comment_id": 1,
    "comment": "Lindo, nos faz refletir sobre a vida, os anos, envelhecer. Vale a pena assistir"
}
```

```sh
// RESPONSE STATUS 200 OK

{
    "id": 11,
    "user": {
        "id": 1,
        "first_name": "John",
        "last_name": "Wick"
    },
    "comment": "Lindo, nos faz refletir sobre a vida, os anos, envelhecer. Vale a pena assistir"
}
```
