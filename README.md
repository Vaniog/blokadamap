# Blokadamap

Чтобы запустить у себя:

####  3. Напрямую (консоль bash)

У вас должен быть локально поднят postgres. Если вам не хочется этого делать, советую запускать через Docker

1. Создайте файл .env скопировав .env.example,
2. Определите переменные окружения


    # На данный момент версия Python 3.10
    # Создание виртуального окружения
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements/requirements.txt

    # Запуск
    ./scripts/start-dev.sh

    # Тесты
    ./scripts/tests/test-mock-ping.sh

#### 3. Через Docker (теперь это удобно)
    
1. Устанавливаете докер 
2. Копируете docker/.env.docker.example в /docker/.env.docker и определяете переменные окружения (можно оставить как есть)


    # build
    ./scripts/docker/build-dev.sh
    # up
    ./scripts/docker/run-dev.sh
    # Тесты
    ./scripts/tests/test-mock-ping.sh
    
    
На 8080 порту запустится приложение fastapi, на 5432 postgres, на 1000 adminer (супер легковесный веб интерфейс для взаимодействия с базой)