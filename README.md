# Блог-платформа

## Описание проекта

Этот проект представляет собой блог-платформу, где пользователи могут регистрироваться, публиковать статьи, комментировать, а также управлять своим контентом.

## Технологический стек

- **Backend**: Django 5.0, Django REST framework, PostgreSQL/SQLite
- **Frontend**: Vue.js 3.0, Vue Router, Vuex, Axios, Tailwind CSS/Vuetify

## Функциональные возможности

1. **Пользователи**
   - Регистрация
   - Авторизация
   - Управление профилем

2. **Статьи**
   - Создание статьи
   - Редактирование статьи
   - Удаление статьи
   - Просмотр статьи

3. **Комментарии**
   - Добавление комментариев к статьям
   - Редактирование комментариев
   - Удаление комментариев

4. **Категории и теги**
   - Добавление категорий и тегов к статьям
   - Фильтрация статей по категориям и тегам

5. **Панель администратора**
   - Управление пользователями
   - Управление статьями и комментариями

## Установка и запуск проекта

### Backend

1. Клонируйте репозиторий:
    ```sh
    git clone https://github.com/yourusername/blog-platform.git
    cd blog-platform
    ```

2. Установите виртуальное окружение и активируйте его:
    ```sh
    python -m venv venv
    source venv/bin/activate  # для Windows используйте venv\Scripts\activate
    ```

3. Установите зависимости:
    ```sh
    pip install -r requirements.txt
    ```

4. Примените миграции:
    ```sh
    python manage.py migrate
    ```

5. Запустите сервер разработки:
    ```sh
    python manage.py runserver
    ```

### Frontend

1. Перейдите в директорию frontend:
    ```sh
    cd frontend
    ```

2. Установите зависимости:
    ```sh
    npm install
    ```

3. Запустите сервер разработки:
    ```sh
    npm run serve
    ```

