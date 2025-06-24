import os
import django
import logging
from telegram.ext import Updater, CommandHandler
from telegram import Update
from telegram.ext import CallbackContext
from decouple import config

# Django setup
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from api.models import TelegramUser  # we'll create this model

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(update: Update, context: CallbackContext):
    username = update.effective_user.username or f"id_{update.effective_user.id}"
    
    # Ensure username is not None before saving
    if username:
        TelegramUser.objects.get_or_create(username=username)
        update.message.reply_text(f"Hi {username}! You’ve been registered.")
    else:
        update.message.reply_text("Failed to register. No username found.")

def main():
    updater = Updater(config('TELEGRAM_BOT_TOKEN'), use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
