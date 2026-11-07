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
    @bot.on.message(AttachmentTypeRule(["photo", "doc", "sticker"]))
    async def attachment_handler(message: Message):
        attachment = message.attachments[0]

        att_type = attachment.type.value if hasattr(attachment.type, "value") else attachment.type

        if att_type == "photo":
            logger.info(f"Пользователь {message.from_id} прислал фото")
            await message.answer(
                bot_text.THIS_IS_PHOTO.format(
                    user_id=message.from_id,
                    photo_id=attachment.photo.id,
                    photo_owner_id=attachment.photo.owner_id,
                )
            )
        elif att_type == "doc":
            logger.info(f"Пользователь {message.from_id} прислал документ")
            await message.answer(
                bot_text.THIS_IS_DOC.format(
                    user_id=message.from_id,
                    doc_id=attachment.doc.id,
                    doc_owner_id=attachment.doc.owner_id,
                    doc_title=attachment.doc.title,
                )
            )
        elif att_type == "sticker":
            logger.info(f"Пользователь {message.from_id} прислал стикер")
            await message.answer(
                bot_text.THIS_IS_STICKER.format(
                    user_id=message.from_id,
                    sticker_id=attachment.sticker.sticker_id,
                )
            )
        else:
            await message.answer("Это вложение я пока не умею обрабатывать")