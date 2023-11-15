# Blokadamap

Чтобы запустить у себя:

1. Создайте файл .env скопировав .env.example,
2. Определите переменные окружения (на данный момент существенна только DATABASE_URL)

####  3. Напрямую (консоль bash)

    # На данный момент версия Python 3.10
    # Создание виртуального окружения
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements/requirements.txt

    # Запуск
    ./scripts/start-dev.sh

    # Тесты
    ./tests/test-mock-ping.sh

#### 3. Через Docker (скорее всего это не понадобится)
    
    ./scripts/docker/build.sh
    ./scripts/docker/run.sh
