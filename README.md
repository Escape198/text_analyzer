# TextAnalyzer

**TextAnalyzer** - это веб-приложение на Django, которое позволяет загружать текстовые файлы и обрабатывать их в фоновом режиме с использованием Celery и Redis.

## Стек технологий

- Django
- Django Rest Framework
- Celery
- Redis
- PostgreSQL
- Docker
- Docker Compose

## Функциональные возможности

- Загрузка текстовых файлов через API.
- Обработка файлов в фоновом режиме с подсчетом количества слов.
- Хранение результатов в базе данных.
- Доступ к результатам API.


```bash
docker-compose build
docker-compose run web python manage.py migrate
docker-compose up
```

Приложение будет доступно по адресу http://localhost:8000.

Загрузка файла
```bash
POST /uploads/
Content-Type: multipart/form-data
Body:
  file: <ваш_текстовый_файл>
```
Запуск Celery worker
```bash
docker-compose run celery
```
Запуск Celery beat
```bash
docker-compose run celery-beat
```# text_analyzer
