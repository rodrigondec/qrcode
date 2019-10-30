################################################################################
# Docker-compose django service commands for dev
################################################################################
current_dir = $(notdir $(shell pwd))

run:
	docker-compose run django $(cmd)

flake8:
	docker-compose run django flake8

migrate:
	docker-compose run django python manage.py migrate $(app)

makemigrations:
	docker-compose run django python manage.py makemigrations

test:
	docker-compose run django python manage.py test $(app)

bash:
	docker-compose run django bash

shell:
	docker-compose run django python manage.py shell

coverage:
	docker-compose run django coverage run --source='.' manage.py test $(app)
	docker-compose run django coverage report

up:
	docker-compose up -d

logs:
	docker-compose logs -f

down:
	docker-compose down

django.stop:
	docker stop django

django.restart: django.stop up

build:
	docker-compose build

build.prod:
	docker-compose -f docker-compose.prod.yml build

up.prod:
	docker-compose -f docker-compose.prod.yml up -d

logs.prod:
	docker-compose -f docker-compose.prod.yml logs -f

down.prod:
	docker-compose -f docker-compose.prod.yml down

config.env:
	cp .env.example .env
	touch .nginx/error.log

remove.volumes:
	docker-compose down
	docker volume rm $(current_dir)_pg_volume

clear.python:
	find . -type d -name __pycache__ -o \( -type f -name '*.py[co]' \) -print0 | xargs -0 rm -rf

clear.docker:
	docker ps | awk '{print $$1}' | grep -v CONTAINER | xargs docker stop

################################################################################
# Populate commands
################################################################################
populate.superuser:
	docker-compose run django python manage.py populate_superuser

################################################################################
# Local commands
################################################################################
pip.install:
	pip install -r requirements-dev.txt

################################################################################
# Heroku commands
################################################################################
deploy:
	git push heroku
