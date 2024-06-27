# Используем официальный образ PostgreSQL как базовый - в 2024 году в РФ dockerhub заблокирован, поэтому через обходные пути
FROM dockerhub.timeweb.cloud/library/postgres:latest

# Устанавливаем переменные окружения для базы данных
ENV POSTGRES_DB=products
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=password

EXPOSE 19432


# Инструкция
# 1. docker build -t pg-asyncio-book .
# 2. docker run -d -p 19432:19432 pg-asyncio-book
# после этого есть контейнер к которому можно подключиться на порту 19432
