import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from vkbottle.bot import Bot, Message
from random import randint
import bot_text
from utils.logger import logger

async def register_handlers(bot: Bot):
    """Регистрирует игровые обработчики"""
    
    @bot.on.message(text=["Бросок", "Кубик", "бросок", "кубик"])
    async def roll_one_dice(message: Message):
        number = randint(1, 6)
        await message.answer(bot_text.DICE_MESSAGE.format(number))
    
    @bot.on.message(text=["Бросок <count>", "Кубик <count>"])
    async def handler_many_dice(message: Message, count: str):
        if count.isdigit():
            number = int(count)
            if number > 2:
                await message.answer("Максимум 2 кубика!")
            elif number == 2:
                num1 = randint(1, 6)
                num2 = randint(1, 6)
                await message.answer(f"Выпало: {num1} и {num2}, сумма: {num1 + num2}")
            else:
                await message.answer("Введите 1 или 2.")
        else:
            await message.answer("Пожалуйста, введите число после слова 'Бросок'.")