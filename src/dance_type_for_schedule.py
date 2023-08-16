import logging

from aiogram.dispatcher import FSMContext
from aiogram.types import (CallbackQuery)
from keyboards import inline_kb_finish

from aiogram import types

from src.create_bot import bot
from load_data import get_sheet_data
from utils import generate_schedule_message

logging.basicConfig(level=logging.INFO)


async def process_dance_type(callback_query: CallbackQuery, state: FSMContext):
    selected_dance_type = callback_query.data.split('_')[1]
    await state.update_data(selected_dence_type=selected_dance_type)
    chat_id = callback_query.from_user.id
    data = get_sheet_data('groups')

    if selected_dance_type == 'бачата':
        bachata_message = generate_schedule_message(data, 'Бачата')
        await bot.send_message(chat_id=chat_id,
                               text=bachata_message,
                               parse_mode=types.ParseMode.MARKDOWN,
                               reply_markup=inline_kb_finish)

    if selected_dance_type == 'кизомба':
        kizomba_message = generate_schedule_message(data, 'Кизомба')
        await bot.send_message(chat_id=chat_id,
                               text=kizomba_message,
                               parse_mode=types.ParseMode.MARKDOWN,
                               reply_markup=inline_kb_finish)
    await callback_query.answer()
