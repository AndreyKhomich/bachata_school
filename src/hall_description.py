import logging
from aiogram import types
from utils import send_hall_info

logging.basicConfig(level=logging.INFO)


async def process_dance_hall_description(callback_query: types.CallbackQuery):
    selected_hall = callback_query.data.split('_')[1]
    chat_id = callback_query.message.chat.id

    if selected_hall == 'первый':
        await send_hall_info(chat_id, hall_number=1)
    elif selected_hall == 'второй':
        await send_hall_info(chat_id, hall_number=2)
    elif selected_hall == 'третий':
        await send_hall_info(chat_id, hall_number=3)
    await callback_query.answer()
