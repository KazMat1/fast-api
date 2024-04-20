## Build an environment

## Create a definition file of packages
- Only Answer a 'n' when you're asked a question about an author
- When asked other questions, you press a enter

### you can choose commands whichever you like
```shell
# through a docker compose command
docker-compose run \
  --entrypoint "poetry init \
    --name demo-app \
    --dependency fastapi \
    --dependency uvicorn[standard]" \
  demo-app
```
```shell
# through a make command
make poerty-init
```
## Install packages based on it
```shell
# through a docker compose command
docker-compose run --entrypoint "poetry install --no-root" demo-app
```
```shell
# through a make command
make poerty-install
```
