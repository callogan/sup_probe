# Система управления проектами
Платформа должна помочь вести проекты которые реализуются в рамках стажировки молодых специалистов.

Аналитика успеваемости стажёров.

Собственная система ведения задач. По причине блокировок пользователей такими ресурсами как Trello и ограничение на использование на подобных ресурсах.

Управление командами и участниками стажировки.

## Старт
    переименовать
    .env.example на .env

### Запустить сборку
```
docker-compose up --build
```

### Alembic migrate
Не выключая контейнеры выполнить команду
```
docker exec -it sup-back alembic upgrade head
```

### Перейти по адресу
```
http:\\127.0.0.1:8000\docs
```

## Alembic создание migrations
Не выключая контейнеры выполнить команду
```
docker exec -it sup-back alembic revision --autogenerate -m 'название модели или миграции'
```

## Инструменты
- Python 3.12
- FastAPI
- SqlAlchemy
- Postgres
- Alembic
- Docker
