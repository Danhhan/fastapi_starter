PRODUCT_COMPOSE_FILE=docker/docker-compose.yml

start:
	docker compose -f $(PRODUCT_COMPOSE_FILE) up -d

build:
	docker compose -f $(PRODUCT_COMPOSE_FILE) up --build

logs:
	docker compose -f $(PRODUCT_COMPOSE_FILE) logs -f

down:
	docker compose -f $(PRODUCT_COMPOSE_FILE) down -v