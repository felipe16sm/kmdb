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
