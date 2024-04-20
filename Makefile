hello:
	echo 'hello world'
up:
	docker compose up
upd:
	docker compose up -d
build:
	docker compose build
build-no-cache:
	docker compose build --no-cache
down:
	docker compose down
downv:
	docker compse down -v
stop:
	docker compose stop
project-init:
	@build
	@poetry-init
	@poetry-install

# Author のみ n. それ以外はenter
poetry-init:
	docker-compose run \
	--entrypoint "poetry init \
		--name demo-app \
		--dependency fastapi \
		--dependency uvicorn[standard]" \
	demo-app
poetry-install:
	docker compose run --entrypoint "poetry install --no-root" demo-app
poetry-add:
	docker compose exec demo-app poetry add $(wordlist 2, $(words $(MAKECMDGOALS) - 2), $(MAKECMDGOALS))
migrate:
	docker compose exec demo-app poetry run python -m api.migrate_db
db:
	docker-compose exec db bash
demo-app:
	docker-compose exec demo-app bash
mysql:
	docker-compose exec db mysql demo
