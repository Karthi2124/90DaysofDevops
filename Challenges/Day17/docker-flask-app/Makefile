.PHONY: build up down logs test clean

build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down

logs:
	docker-compose logs -f

test:
	docker-compose exec web python -m pytest

clean:
	docker system prune -f
	docker volume prune -f