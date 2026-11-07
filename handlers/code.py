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
        
async def register_content_handler(bot: Bot):
    @bot.on.message()
    async def content_handler(message: Message):
        if not message.attachments:
            await message.answer("Пришли фотографию 📷")
            return

        photo = None
        doc = None
        
        for attachment in message.attachments:
            att_type = attachment.type.value if hasattr(attachment.type, "value") else attachment.type
            
            if att_type == "photo":
                photo = attachment.photo
            elif att_type == "doc":
                doc = attachment.doc

        if photo is None:
            if doc:
                await message.answer(
                    f"Это документ 📄\n"
                    f"Название: {doc.title}\n"
                    f"Расширение: {doc.ext}\n"
                    f"Размер: {doc.size} байт"
                )
            else:
                await message.answer("Я пока умею архивировать только фотографии.")
            return

        big = max(photo.sizes, key=lambda s: s.width * s.height)
        
        report = (
            f"📸 Фото найдено!\n"
            f"ID: {photo.id}\n"
            f"Owner ID: {photo.owner_id}\n"
            f"Вариантов размера: {len(photo.sizes)}\n"
            f"Максимальный размер: {big.width}×{big.height}\n"
            f"Фото сохранено в архив урока ✅"
        )
        await message.answer(report)