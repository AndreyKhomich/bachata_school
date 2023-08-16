from database.database_manager import get_user_subscription
from keyboards import inline_kb_finish
from src.create_bot import bot

alert_text = """
Вы видите это сообщение по одной из причин:

1) Вы указали разные номера телефонов при регистрации у администратора и в чат-боте.
В этом случае, пожалуйста, проверьте эту информацию и перерегистрируйтесь в чат-боте.

2) Срок действия вашего абонемента истек.
Вы можете приобрести новый абонемент.

3) У вас есть активный абонемент, но данные еще не обновились.
Попробуйте узнать информацию о вашем абонементе позднее.

4) Вы впервые посетили наш бот.
Вы можете записаться на пробное занятие.
"""


def generate_schedule_message(data, dance_type):
    schedule_message = "Расписание групп:\n\n"

    for item in data:
        if item['Название танца'] == dance_type:
            address = item['Адрес']
            day = item['День']
            time = item['Время']
            start_date = item['Дата старта группы']
            teachers = item['Преподаватели']
            group_experience = item['Стаж группы']

            group_info = (
                f"**Адрес:** {address}\n"
                f"**День:** {day}\n"
                f"**Время:** {time}\n"
                f"**Дата старта группы:** {start_date}\n"
                f"**Преподаватели:** {teachers}\n"
                f"**Стаж группы:** {group_experience}\n\n"
            )

            schedule_message += group_info

    return schedule_message


async def display_subscription_data(user_id):
    user_subscription = await get_user_subscription(user_id)

    if user_subscription:
        subscription_message = f"Ваш абонимент:\n" \
                               f"Посещено занятий: {user_subscription.visited_classes}\n" \
                               f"Всего занятий: {user_subscription.classes}\n" \
                               f"Осталось занятий: {user_subscription.remaining_classes}\n" \
                               f"Дата окончания: {user_subscription.date}"
    else:
        subscription_message = "У вас нет активного абонимента."

    return subscription_message


async def display_prices():
    subscription_data = {
        "Первый абонемент": {
            "description": "Для тех, кто ранее не занимался в нашей школе. Максимум 8 часов занятий в течение 30 дней.",
            "standard_price": "95 р.",
            "discount_price": "80 р.",
            "discount_info": "Скидка 15 р. при покупке на первом пробном занятии."
        },
        "Стандартный абонемент": {
            "description": "Максимум 8 часов занятий в течение 30 дней.",
            "standard_price": "95 р.",
            "discount_price": "90 р.",
            "discount_info": "Скидка - 5 р. при оплате ДО окончания старого абонемента."
        },
        "MAX24/60": {
            "description": "Максимум 24 часа занятий в течение 60 дней.",
            "standard_price": "220 р.",
            "discount_price": "190 р.",
            "discount_info": "Для учеников, которые занимаются больше 3 месяцев"
        },
        "Трехмесячный (24/90)": {
            "description": "Максимум 24 часа занятий в течение 90 дней.",
            "standard_price": "240 р.",
            "discount_price": "210 р.",
            "discount_info": "Для учеников, которые занимаются больше 3 месяцев"
        },
    }

    message = "АБОНЕМЕНТЫ\tСТОИМОСТЬ\tСКИДКИ\n\n"

    for subscription, data in subscription_data.items():
        description = data["description"]
        standard_price = data["standard_price"]
        discount_price = data["discount_price"]
        discount_info = data["discount_info"]

        message += f"{subscription}\n{description}\n"
        message += f"Стоимость стандартного абонемента:\n{standard_price}\n"
        message += f"Цена со скидкой:\n{discount_price} - {discount_info}\n\n\n"

    return message


async def send_hall_info(chat_id: int, hall_number: int):
    general_description = "Для того чтобы забронировать зал, обращайтесь к администратору по номеру +375446666666.\n\n"\
                          "Актуально расписание можно посмотреть в разделе Свободны залы."

    dance_halls = [
        {
            'name': 'Танцевальный Зал "Ритм"',
            'price': 'Стоимость: 15 рублей в час',
            'size': 'Размер: 100 кв. м.',
            'photo': 'https://ibb.co/VWc36sL'
        },
        {
            'name': 'Танцевальный Зал "Энергия"',
            'price': 'Стоимость: 20 рублей в час',
            'size': 'Размер: 120 кв. м.',
            'photo': 'https://ibb.co/fXrb5ds'
        },
        {
            'name': 'Танцевальный Зал "Хореография"',
            'price': 'Стоимость: 25 рублей в час',
            'size': 'Размер: 150 кв. м.',
            'photo': 'https://ibb.co/PhxFfzS'
        }
    ]

    hall_info = dance_halls[hall_number - 1]

    caption = f"{general_description}\n\n{hall_info['name']}\n{hall_info['price']}\n{hall_info['size']}"
    await bot.send_photo(chat_id=chat_id,
                         photo=hall_info['photo'],
                         caption=caption,
                         reply_markup=inline_kb_finish)
