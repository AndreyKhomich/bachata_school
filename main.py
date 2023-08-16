
import logging

from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from src.create_bot import dp, bot, bot_token, port
from src.dance_type_for_schedule import process_dance_type
from src.hall_description import process_dance_hall_description
from src.helpers import handle_unexpected_messages
from src.menu import process_menu, handle_new_section_or_finish
from src.payment_handler import process_payment_option, process_middle_subscription, process_high_subscription
from src.registration import start, process_last_name, AuthStates, process_age, process_user_data, process_first_name, \
    cancel_registration

logging.basicConfig(level=logging.INFO)


dp.register_message_handler(start, Command("start"), state=['*', 're_registration'])
dp.register_callback_query_handler(cancel_registration, lambda c: c.data.startswith('отмена_'), state='*')
dp.register_callback_query_handler(process_menu, lambda c: c.data.startswith('меню_'), state='menu_option')

dp.register_callback_query_handler(process_payment_option, lambda c: c.data.startswith('оплата_'), state='payment')
dp.register_callback_query_handler(process_middle_subscription, lambda c: c.data.startswith('срок_'), state='middle_subscription')
dp.register_callback_query_handler(process_high_subscription, lambda c: c.data.startswith('срок_'), state='high_subscription ')

dp.register_callback_query_handler(process_dance_type, lambda c: c.data.startswith('танец_'), state='dance_type')

dp.register_callback_query_handler(process_dance_hall_description, lambda c: c.data.startswith('зал_'), state='halls')

dp.register_message_handler(process_first_name, lambda message: message.text.isalpha(), state=AuthStates.waiting_for_first_name)
dp.register_message_handler(process_last_name, lambda message: message.text.isalpha(), state=AuthStates.waiting_for_last_name)
dp.register_message_handler(process_age, lambda message: message.text.isdigit(), state=AuthStates.waiting_for_age)
dp.register_message_handler(process_user_data, lambda message: message.text.isdigit(), state=AuthStates.waiting_for_phone_number)

dp.register_message_handler(handle_unexpected_messages, state='*')
dp.register_callback_query_handler(handle_new_section_or_finish, lambda c: c.data.startswith('новый_'), state='*')


async def run_bot(dispatcher: Dispatcher):
    await bot.set_webhook(url=f"https://zodiacbot.herokuapp.com/webhook/{bot_token}", drop_pending_updates=True)
    await bot.set_webhook(url=None)
    await dispatcher.start_polling()


if __name__ == '__main__':
    executor.start_webhook(
        dispatcher=dp,
        webhook_path=f'/webhook/{bot_token}',
        on_startup=run_bot,
        skip_updates=True,
        host='0.0.0.0',
        port=port
    )
