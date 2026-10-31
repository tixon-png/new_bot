import os
from dotenv import load_dotenv

# Загружаем переменные из .env
load_dotenv()

# Токен бота
BOT_TOKEN = os.getenv("MY_TOKEN")

# Проверка, что токен загружен
if not BOT_TOKEN:
    raise ValueError("❌ Токен не найден! Проверь файл .env")