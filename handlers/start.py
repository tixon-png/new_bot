import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from keyboards.main_kb import get_main_keyboard
from vkbottle.bot import Bot, Message
import bot_text
from utils.logger import logger

async def register_handlers(bot: Bot):
    """Регистрирует обработчики команд"""
    
    @bot.on.message(command="start")
    async def start_handler(message: Message):
        logger.info(f"Пользователь {message.from_id} вызвал /start")
        await message.answer(bot_text.START_MESSAGE)

    @bot.on.message(command="help")
    async def help_handler(message: Message):
        logger.info(f"Пользователь {message.from_id} вызвал /help")
        await message.answer(bot_text.HELP_MESSAGE)
        
    @bot.on.message(text=["Привет", "привет", "Приивт", "привт", "ку","старт"])
    async def greeting_handler(message: Message):
        text = (message.text or "")
        if message.text in text:
            await message.answer(bot_text.START_MESSAGE, keyboard=get_main_keyboard())

    @bot.on.message(text=["Пока", "пока", "бб"])
    async def bye_handler(message: Message):
        await message.answer("Досвидания! Бот закрылся.")
        
    @bot.on.message(command="info")
    async def info_handler(message: Message):
        await message.answer(bot_text.INFO_MESSAGE)
        
    @bot.on.message(text="Мой ID")
    async def id_handler(message: Message):
        
        user_id = message.from_id
        users = await message.ctx_api.users.get(
        user_ids=user_id)
        first_name = users[0].first_name
        await message.answer(f"Привет, {first_name}! Вот твой айди - {user_id}")
        

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