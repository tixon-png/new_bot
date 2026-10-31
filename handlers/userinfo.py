from vkbottle.bot import Message


async def cmd_me(message: Message):
    user_id = message.from_id
    users = await message.ctx_api.users.get(
        user_ids=user_id
    )
    first_name = users[0].first_name

    await message.answer(f"Привет, {first_name}!")


async def register_handlers(bot):
    bot.on.message(text=["/me", "кто я", "как меня зовут"])(cmd_me)