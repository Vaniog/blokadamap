# Blokadamap

Чтобы запустить у себя:

####  Напрямую (консоль bash)

У вас должен быть локально поднят postgres. Если вам не хочется этого делать, советую запускать через Docker

1. Создайте файл .env скопировав .env.example,
2. Определите переменные окружения

```
    # На данный момент версия Python 3.10
    # Создание виртуального окружения
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements/requirements.txt

    # Запуск
    ./scripts/start-dev.sh

    # Тесты
    ./scripts/tests/test-mock-ping.sh
```

#### Через Docker (теперь это удобно)
    
1. Устанавливаете докер 
2. Копируете .env.example в .env и определяете переменные окружения (можно оставить как есть)

```
    # build
    docker compose build
    # up
    docker compose up
```
    
На 8080 порту запустится приложение fastapi, на 5432 postgres, 
на 1000 adminer (супер легковесный веб интерфейс для взаимодействия с базой)

#### Про adminer:
Если запуск получится, то на localhost:1000 будет запущен adminer \
Если вы не меняли .env.example при копировании, то credentials для доступа такие:

    System: PostgreSQL
    Server: database
    Username: root
    Password: root
    Database: db

P.s. Неочевидный нюанс в том, что server это database, а не localhost,
это связано с тем, что контейнеры для себя создают свою сеть, и в этой сети нету localhost.
Вместо этого в качестве адресов контейнеров выступают названия их как сервисов (как прописано в docker-compose.yaml) 
P.p.s На самом деле вроде можно и localhost, можете проверить