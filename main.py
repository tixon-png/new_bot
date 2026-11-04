import asyncio
from vkbottle import *
from config import BOT_TOKEN
from utils.logger import logger
from handlers import start, echo, games, code


async def main():
    """Основная функция запуска бота"""
    
    # Создаём бота
    bot = Bot(token=BOT_TOKEN)
    
    logger.info("🚀 Запуск бота...")
    logger.info(f"Token: {BOT_TOKEN[:20]}...")
    
    # Регистрируем все обработчики
    # Порядок важен: echo должен быть последним!
    await code.register_handlers(bot)
    await start.register_handlers(bot)
    await games.register_handlers(bot)
    await echo.register_handlers(bot)
    
    logger.info("✅ Все обработчики зарегистрированы")
    logger.info("🤖 Бот запущен и слушает сообщения...")
    
    # Запускаем бота
    await bot.run_polling()

if __name__ == "__main__":
    asyncio.run(main())