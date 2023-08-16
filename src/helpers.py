from aiogram import types
from src.create_bot import dp


async def handle_unexpected_messages(message: types.Message):
    state = dp.current_state(user=message.from_user.id)
    if await state.get_state() is not None:
        await message.reply("Пожалуйста, используйте кнопки для взаимодействия с ботом.")
    else:
        await message.reply("Неизвестная команда. Для начала работы с ботом используйте /start.")
