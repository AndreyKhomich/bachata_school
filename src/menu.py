
from aiogram.dispatcher import FSMContext
from aiogram.types import (CallbackQuery)

from database.database_manager import delete_user_with_data
from keyboards import inline_kb_menu, inline_dance_menu, inline_kb_finish, inline_kb_free_hall, inline_kb_payment, \
    inline_kb_halls

from aiogram import types

from src.create_bot import bot
from src.about_us import school_description
from utils import display_subscription_data, display_prices, alert_text


async def process_menu(callback_query: CallbackQuery, state: FSMContext):
    selected_menu_option = callback_query.data.split('_')[1]
    await state.update_data(selected_menu_option=selected_menu_option)
    chat_id = callback_query.from_user.id

    if selected_menu_option == 'расписание':
        await bot.send_message(
            chat_id=chat_id,
            text="Выберите танец:",
            reply_markup=inline_dance_menu
        )
        await state.set_state('dance_type')

    if selected_menu_option == 'афиша':
        await state.set_state('poster')

    if selected_menu_option == 'абонимент':
        await state.set_state('subscription')
        subscription_message = await display_subscription_data(chat_id)
        if subscription_message != 'У вас нет активного абонимента.':
            await bot.send_message(chat_id=chat_id,
                                   text=subscription_message,
                                   parse_mode=types.ParseMode.MARKDOWN,
                                   reply_markup=inline_kb_finish)
        else:
            await bot.send_message(chat_id=chat_id,
                                   text=alert_text,
                                   parse_mode=types.ParseMode.MARKDOWN,
                                   reply_markup=inline_kb_finish)
            await state.set_state('menu_option')

    if selected_menu_option == 'цены':
        text = await display_prices()
        await bot.send_message(chat_id=chat_id,
                               text=text,
                               parse_mode=types.ParseMode.MARKDOWN,
                               reply_markup=inline_kb_finish)

    if selected_menu_option == 'котнакты':
        text = school_description
        await bot.send_message(chat_id=chat_id,
                               text=text,
                               parse_mode=types.ParseMode.MARKDOWN,
                               reply_markup=inline_kb_finish)

    if selected_menu_option == 'оплата':
        await bot.send_message(chat_id=chat_id,
                               text="Пожалуйста выберите тип абонимента:",
                               parse_mode=types.ParseMode.MARKDOWN,
                               reply_markup=inline_kb_payment)
        await state.set_state('payment')

    if selected_menu_option == 'зал':
        await bot.send_message(chat_id=chat_id,
                               text="Пожалуйста выберите номер зала. Для брорнирования зала"
                                    " свяжитесь с администратором по номеру +375446666666",
                               parse_mode=types.ParseMode.MARKDOWN,
                               reply_markup=inline_kb_free_hall)
        await state.set_state('menu_option')

    if selected_menu_option == 'регистрация':
        await delete_user_with_data(chat_id)
        await bot.send_message(chat_id=chat_id,
                               text="Для перерегистрации нажмите команду /start",
                               parse_mode=types.ParseMode.MARKDOWN
                               )
        await state.set_state('re_registration')

    if selected_menu_option == 'залы':
        if selected_menu_option == 'залы':
            await bot.send_message(chat_id=chat_id,
                                   text="Пожалуйста выберите номер зала.",
                                   parse_mode=types.ParseMode.MARKDOWN,
                                   reply_markup=inline_kb_halls)
            await state.set_state('halls')
        await state.set_state('halls')
    await callback_query.answer()


async def handle_new_section_or_finish(callback_query: CallbackQuery, state: FSMContext):
    selected_option = callback_query.data.split('_')[1]
    chat_id = callback_query.from_user.id

    if selected_option == 'обратно':
        await bot.send_message(chat_id=chat_id,
                               text=" Пожалуйста используйте меню для взаимодействия с ботом.",
                               reply_markup=inline_kb_menu
                               )
        await state.set_state('menu_option')
    elif selected_option == 'закончить':
        await bot.send_message(chat_id=chat_id,
                               text="Спасибо что воспользовались нашим ботом!\n\n"
                                    "Для повторного общения нажмите на ссылку: /start")
        await state.finish()

    await callback_query.answer()
