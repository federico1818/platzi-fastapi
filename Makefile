SHELL = /bin/sh

PHONY: install start stop in

install:
	@docker compose -f docker/docker-compose.yml -p platzi-fastapi \
		run --rm fastapi pip install -r /config/requirements.txt

start:
	@docker compose -f docker/docker-compose.yml -p platzi-fastapi up -d

stop:
	@docker compose -f ./docker/docker-compose.yml -p platzi-fastapi down

in:
	@docker exec -it platzi-fastapi bash

build:
	@if [ -z "$(version)" ]; then \
		echo "Falta el parámetro 'version'. Ejemplo: make build version=v1.0.0"; \
		exit 1; \
	fi; \
	./deploy/deploy.sh $(version)
	@echo "Done"