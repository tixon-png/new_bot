import sys
from pathlib import Path

# Добавляем родительскую директорию в путь поиска модулей
sys.path.append(str(Path(__file__).parent.parent))

from vkbottle import Bot
from vkbottle.bot import Message
from vkbottle.dispatch.rules.base import AttachmentTypeRule
import bot_text
from utils.logger import logger

async def register_handlers(bot: Bot):
    async def code_handler(message: Message):
    
        if not message.attachments:
            if message.text:
                await message.answer(f"Пользователь {message.from_id}, прислал сообщение.")
            else:
                await message.answer("Мне нужно прислать (фото,документ)")
    @bot.on.message()
    async def start_handler(message: Message):
        await message.answer(f"{bot_text.START_MESSAGE}\nкол-во вложений{len(message.attachments)}")
        
