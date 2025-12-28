SHELL = /bin/sh

PHONY: install start stop in

install:
	@docker compose -f docker/docker-compose.yml -p platzi-fastapi \
		run --rm fastapi pip install -r requirements.txt

start:
	@docker compose -f docker/docker-compose.yml -p platzi-fastapi up -d

stop:
	@docker compose -f ./docker/docker-compose.yml -p platzi-fastapi down

in:
	@docker exec -it platzi-fastapi bash