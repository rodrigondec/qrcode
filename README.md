# Qr Coder project
Project made with Django + PostgreSQL + qrcode

[![License](https://img.shields.io/github/license/rodrigondec/rctech)](https://img.shields.io/github/license/rodrigondec/rctech)

# Install
## Docker + docker-compose
Install [docker-ce](https://docs.docker.com/install/) and [docker-compose](https://docs.docker.com/compose/install/) from each documentation

### Setting up
On the project folder run the following commands:
1. `$ make config.env` to copy the file `.env.example` to `.env`
2. `$ make build` to build docker containers

# Running the project
Simply run the command `$ make up` and *voilà*.

This command will start 3 services on your machine:
- Django server on [http://0.0.0.0:8000](http://0.0.0.0:8000)
- PgAdmin server on [http://0.0.0.0:5050](http://0.0.0.0:5050)
- PostgreSQL service on port [5432]()

## Tests
On the project folder:
- run the command `$ make test` or `$ make test app=$(app_name)`. You may run the command `$ make coverage` instead.
- run the command `$ make flake8`

## Administration
Django Admin Site is enabled for the project on [http://0.0.0.0:8000/admin](http://0.0.0.0:8000/admin).

The command `$ make populate.superuser` may be used to create the superuser `User(username='superuser', password='@Admin123')`.
