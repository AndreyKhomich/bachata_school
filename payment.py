import logging

from aiogram import  types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ContentType

from src.create_bot import bot, dp

logging.basicConfig(level=logging.INFO)


inline_kb_payment = InlineKeyboardMarkup()
inline_kb_payment.add(InlineKeyboardButton("Pay", pay=True))
inline_kb_payment.add(InlineKeyboardButton("Выбрать новый раздел", callback_data="новый_обратно"))
inline_kb_payment.add(InlineKeyboardButton("Закончить общение", callback_data="новый_закончить"))


async def initiate_payment_standard(chat_it):
    PRICE = types.LabeledPrice(label="Абонемент на 8 занятий", amount=95 * 100)
    await bot.send_invoice(chat_it,
                           title="Групповой абонимент",
                           description="Это групповой абонимент на 8 занятий для парной группы",
                           provider_token='381764678:TEST:63935',
                           currency="rub",
                           photo_url="https://www.aroged.com/wp-content/uploads/2022/06/Telegram-has-a-premium-subscription.jpg",
                           photo_width=416,
                           photo_height=234,
                           photo_size=416,
                           is_flexible=False,
                           prices=[PRICE],
                           start_parameter="one-month-subscription",
                           payload="test-invoice-payload",
                           reply_markup=inline_kb_payment
                           )


async def initiate_payment_standard_discount(chat_it):
    PRICE = types.LabeledPrice(label="Абонемент на 8 занятий для клиентов с уже имеющимся абониментом", amount=85 * 100)
    await bot.send_invoice(chat_it,
                           title="Групповой абонимент",
                           description="Это групповой абонимент на 8 занятий для парной группы",
                           provider_token='381764678:TEST:63935',
                           currency="rub",
                           photo_url="https://www.aroged.com/wp-content/uploads/2022/06/Telegram-has-a-premium-subscription.jpg",
                           photo_width=416,
                           photo_height=234,
                           photo_size=416,
                           is_flexible=False,
                           prices=[PRICE],
                           start_parameter="one-month-subscription",
                           payload="test-invoice-payload",
                           reply_markup=inline_kb_payment
                           )


async def initiate_payment_medium(chat_it):
    PRICE = types.LabeledPrice(label="Абонемент на 12 занятий с возможностью посещения в течение 60 дней",
                               amount=240 * 100)
    await bot.send_invoice(chat_it,
                           title="Групповой абонимент",
                           description="Это групповой абонимент на 12 занятий для парной группы",
                           provider_token='381764678:TEST:63935',
                           currency="rub",
                           photo_url="https://www.aroged.com/wp-content/uploads/2022/06/Telegram-has-a-premium-subscription.jpg",
                           photo_width=416,
                           photo_height=234,
                           photo_size=416,
                           is_flexible=False,
                           prices=[PRICE],
                           start_parameter="one-month-subscription",
                           payload="test-invoice-payload",
                           reply_markup=inline_kb_payment
                           )


async def initiate_payment_medium_discount(chat_it):
    PRICE = types.LabeledPrice(label="Абонемент на 12 занятий с возможностью посещения в течение "
                                     "60 дней для клиентов которые посещают нашу школу более 3-ех месяцев.",
                               amount=190 * 100)
    await bot.send_invoice(chat_it,
                           title="Групповой абонимент",
                           description="Это групповой абонимент на 12 занятий для парной группы",
                           provider_token='381764678:TEST:63935',
                           currency="rub",
                           photo_url="https://www.aroged.com/wp-content/uploads/2022/06/Telegram-has-a-premium-subscription.jpg",
                           photo_width=416,
                           photo_height=234,
                           photo_size=416,
                           is_flexible=False,
                           prices=[PRICE],
                           start_parameter="one-month-subscription",
                           payload="test-invoice-payload",
                           reply_markup=inline_kb_payment
                           )


async def initiate_payment_high(chat_it):
    PRICE = types.LabeledPrice(label="Абонемент на 12 занятий с возможностью посещения в течение 90 дней",
                               amount=240 * 100)
    await bot.send_invoice(chat_it,
                           title="Групповой абонимент",
                           description="Это групповой абонимент на 12 занятий для парной группы",
                           provider_token='381764678:TEST:63935',
                           currency="rub",
                           photo_url="https://www.aroged.com/wp-content/uploads/2022/06/Telegram-has-a-premium-subscription.jpg",
                           photo_width=416,
                           photo_height=234,
                           photo_size=416,
                           is_flexible=False,
                           prices=[PRICE],
                           start_parameter="one-month-subscription",
                           payload="test-invoice-payload",
                           reply_markup=inline_kb_payment
                           )


async def initiate_payment_high_discount(chat_it):
    PRICE = types.LabeledPrice(label="Абонемент на 12 занятий с возможностью посещения в течение "
                                     "90 дней для клиентов которые посещают нашу школу более 3-ех месяцев.",
                               amount=210 * 100)
    await bot.send_invoice(chat_it,
                           title="Групповой абонимент",
                           description="Это групповой абонимент на 12 занятий для парной группы",
                           provider_token='381764678:TEST:63935',
                           currency="rub",
                           photo_url="https://www.aroged.com/wp-content/uploads/2022/06/Telegram-has-a-premium-subscription.jpg",
                           photo_width=416,
                           photo_height=234,
                           photo_size=416,
                           is_flexible=False,
                           prices=[PRICE],
                           start_parameter="one-month-subscription",
                           payload="test-invoice-payload",
                           reply_markup=inline_kb_payment
                           )


@dp.pre_checkout_query_handler(lambda query: True)
async def pre_checkout_query(pre_checkout_q: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_q.id, ok=True)


@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def successful_payment(message: types.Message):
    print("SUCCESSFUL PAYMENT:")
    payment_info = message.successful_payment.to_python()
    for k, v in payment_info.items():
        print(f"{k} = {v}")

    await bot.send_message(message.chat.id,
                           f"Платеж на сумму {message.successful_payment.total_amount // 100} {message.successful_payment.currency} прошел успешно!!!")

