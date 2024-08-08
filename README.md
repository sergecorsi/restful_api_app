# FastAPI User Management and Task Management API

## Описание

Это пример RESTful API для регистрации, авторизации и управления записями пользователей, использующие технологии:

- Python
- FastAPI
- Redis для хранения данных в NoSQL формате
- PostgreSQL для хранения данных пользователей и их записей
- JWT-токены для проверки авторизации пользователей
- slowapi для ограничения количества запросов
- Docker для контейнеризации приложения (необязательно)

## Установка

### Требования

- Python 3.8+
- PostgreSQL
- Redis
- Установленный Docker (необязательно)

### Шаги установки

1. Клонируйте репозиторий:

git clone <repository_url>
cd <repository_directory>

Создайте виртуальное окружение и активируйте его:

python -m venv venv
source venv/bin/activate   # для Linux/Mac
venv\Scripts\activate      # для Windows

Установите зависимости:

pip install -r requirements.txt
Настройте базу данных PostgreSQL и Redis. 

Настройте переменные окружения в файле .env:

DATABASE_URL=postgresql://<username>:<password>@localhost/<dbname>
SECRET_KEY=your_secret_key
ACCESS_TOKEN_EXPIRE_MINUTES=30
ALGORITHM=HS256

Инициализируйте базу данных:

python init_db.py
Запустите приложение:

uvicorn app.main:app --reload

## Использование:

Регистрация пользователя:  
POST /auth/register

{
  "username": "test_user",
  "password": "test_password"
}

Авторизация пользователя
POST /auth/login

{
  "username": "test_user",
  "password": "test_password"
}
Ответ:

{
  "access_token": "token",
  "token_type": "bearer"
}

Создание новой записи
POST /tasks

Заголовок: Authorization: Bearer <access_token>

{
  "title": "Sample Task",
  "description": "This is a sample task."
}

Получение списка всех записей
GET /tasks

Заголовок: Authorization: Bearer <access_token>

Получение конкретной записи
GET /tasks/{task_id}

Заголовок: Authorization: Bearer <access_token>

Изменение записи
PUT /tasks/{task_id}

Заголовок: Authorization: Bearer <access_token>

{
  "title": "Updated Task",
  "description": "This is an updated task."
}

Удаление записи
DELETE /tasks/{task_id}
Заголовок: Authorization: Bearer <access_token>
