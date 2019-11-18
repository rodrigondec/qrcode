# Qr Coder project
Project made with Django + PostgreSQL + qrcode

[![License](https://img.shields.io/github/license/rodrigondec/rctech)](https://img.shields.io/github/license/rodrigondec/rctech)

# Install
## Docker + docker-compose
Install [docker-ce](https://docs.docker.com/install/) and [docker-compose](https://docs.docker.com/compose/install/) from each documentation

### Setting up
to copy the file `.env.example` to `.env` and create the file `.nginx/error.log` run the following commands:
<details><summary>Linux</summary>

    make config.env
    make config.nginx
or 

    make config.all
</details>

The next step is to build project image
<details><summary>Development image</summary>

    make build
</details>
<details><summary>Production image</summary>

    make build.prod
</details>

# Running the project
Simply run the `up` command of your choice and *voilà*.

<details><summary>Development up</summary>

    make up
This command will start 2 services on your machine:
- Django server on [http://0.0.0.0:8000](http://0.0.0.0:8000)
- PostgreSQL service on port [5432]()

>IMPORTANT NOTE! 
>
>These services are binded to each of your machine respective port
</details>
<details><summary>Production up</summary>

    make up.prod
This command will start 3 services on your machine:
- Django server
- PostgreSQL service
- Nginx service on [http://0.0.0.0](http://0.0.0.0)

>IMPORTANT NOTE! 
>
>Only the nginx service is binded to your machine ports
</details>

## Tests
On the project folder:
- run the command `$ make test` or `$ make test app=$(app_name)`. You may run the command `$ make coverage` instead.
- run the command `$ make flake8`

## Administration
Django Admin Site is enabled for the project on [http://0.0.0.0:8000/admin](http://0.0.0.0:8000/admin) or [http://0.0.0.0/admin](http://0.0.0.0/admin) (depending on `up command`).

The command `$ make populate.superuser` may be used to create the superuser `User(username='superuser', password='@Admin123')`.
