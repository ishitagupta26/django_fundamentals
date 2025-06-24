-->Django Internship Assignment

This project demonstrates backend skills using Django, DRF, Celery, Redis, and Telegram Bot integration.

-->Features

- JWT Authentication (Token & Refresh)
- Public & Protected APIs
- Background task using Celery + Redis
- Telegram Bot stores username on `/start`
- Clean code structure with `.env` configs

-->How to Run Locally

1. Clone the repo  
2. Create virtualenv and activate it  
3. Install dependencies:
   ```bash
   pip install -r requirements.txt

-->Set environment variables in .env:

SECRET_KEY=your_secret_key
DEBUG=False
TELEGRAM_BOT_TOKEN=your_bot_token

-->Run server:

python manage.py runserver

-->Start Celery worker:

celery -A backend worker --loglevel=info --pool=solo

-->Start Telegram bot:

python bot.py

-->Endpoints
1. GET - /api/public/ – Public
2. GET - /api/protected/ – JWT required
3.POST -  /api/token/ – Login (get token)
4.POST - /api/send-email/ – Trigger Celery task
5.Telegram Bot – Send /start to register


-->Tech Stack
Django 5
DRF
Celery
Redis
Telegram Bot API