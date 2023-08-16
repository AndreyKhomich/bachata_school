import logging

from aiogram.dispatcher import FSMContext
from aiogram.types import (CallbackQuery)

from keyboards import inline_kb_term_of_usage
from aiogram import types

from src.create_bot import bot
from payment import initiate_payment_standard, initiate_payment_standard_discount, initiate_payment_medium, \
    initiate_payment_medium_discount, initiate_payment_high, initiate_payment_high_discount

from database.database_manager import get_user_subscription


logging.basicConfig(level=logging.INFO)


async def process_payment_option(callback_query: CallbackQuery, state: FSMContext):
    selected_option = callback_query.data.split('_')[1]
    chat_id = callback_query.from_user.id

    if selected_option == 'стандартный':
        subscription = await get_user_subscription(chat_id)
        if subscription and subscription.remaining_classes > 0:
            await initiate_payment_standard_discount(chat_id)
        else:
            await initiate_payment_standard(chat_id)

    elif selected_option == 'средний':
        await state.set_state('middle_subscription')
        await bot.send_message(chat_id=chat_id,
                               text="Как давно вы занимаетесь в нашей школе:",
                               parse_mode=types.ParseMode.MARKDOWN,
                               reply_markup=inline_kb_term_of_usage)

    elif selected_option == 'большой':
        await state.set_state('high_subscription')
        await bot.send_message(chat_id=chat_id,
                               text="Как давно вы занимаетесь в нашей школе:",
                               parse_mode=types.ParseMode.MARKDOWN,
                               reply_markup=inline_kb_term_of_usage)


async def process_middle_subscription(callback_query: CallbackQuery):
    selected_option = callback_query.data.split('_')[1]
    chat_id = callback_query.from_user.id

    if selected_option == 'мало':
        await initiate_payment_medium(chat_id)

    if selected_option == 'много':
        await initiate_payment_medium_discount(chat_id)
    await callback_query.answer()


async def process_high_subscription(callback_query: CallbackQuery):
    selected_option = callback_query.data.split('_')[1]
    chat_id = callback_query.from_user.id

    if selected_option == 'мало':
        await initiate_payment_high(chat_id)

    if selected_option == 'много':
        await initiate_payment_high_discount(chat_id)
    await callback_query.answer()
