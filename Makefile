up:
	docker compose up
upd:
	docker compose up -d
build:
	docker compose build
build-no-cache:
	docker compose build --no-cache
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
project-init:
	@build
	@poetry-init
	@poetry-install
down:
	docker compose down
downv:
	docker compse down -v
stop:
	docker compose stop
hello:
	echo 'hello world'
