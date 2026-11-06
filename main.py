import asyncio
from vkbottle.bot import Bot
from config import BOT_TOKEN
from utils.logger import logger
from handlers import start, echo, games, code

async def main():
    """Основная функция запуска бота"""

    # Проверка наличия токена (важно для безопасности)
    if not BOT_TOKEN:
        logger.error("❌ BOT_TOKEN не найден! Проверьте файл .env")
        return

    # Создаём бота
    bot = Bot(token=BOT_TOKEN)

    logger.info("🚀 Запуск бота...")

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
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("⛔ Бот остановлен пользователем")
    except Exception as e:
        logger.exception(f"💥 Критическая ошибка: {e}")