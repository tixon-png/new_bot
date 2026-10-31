import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from vkbottle.bot import Bot, Message
from datetime import datetime
import bot_text
from keyboards.main_kb import get_main_keyboard
from utils.logger import logger

async def register_handlers(bot: Bot):
    """Регистрирует эхо-обработчик"""
    # Этот обработчик ловит ВСЁ остальное
    @bot.on.message()
    async def echo_handler(message: Message):
        text = (message.text or "").lower()
        
        if not message.text:
            await message.answer(f"Пользователь {message.from_id}, прислал сообщение.")
        elif "время" in text or "дата" in text:
            await message.answer(f"Текущее время: {datetime.now().strftime('%H:%M:%S')}")
        elif "помощь" in text:
            await message.answer("привет\n мой id\n info for bot")
        elif "секрет" in text or "пароль" in text:
            await message.answer("Я никому не скажу!")
        else:  
            await message.answer(f"Ваш id: {message.from_id}, а длина твоего сообщения: {len(message.text)}")
        
        logger.info(f"Текст: {message.text}, {message.from_id}")