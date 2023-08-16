from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


Inline_btn_payment = InlineKeyboardButton("Оплатить", pay=True)
Inline_btn_menu_back = InlineKeyboardButton("Выбрать новый раздел", callback_data="новый_обратно")
Inline_btn_finish = InlineKeyboardButton("Закончить общение", callback_data="новый_закончить")

inline_kb_finish = InlineKeyboardMarkup(row_width=1)
inline_kb_finish.add(Inline_btn_menu_back).add(Inline_btn_finish)

inline_btn_schedule = InlineKeyboardButton("Расписание занятий", callback_data="меню_расписание")
inline_btn_booking = InlineKeyboardButton("Свободные залы",  callback_data="меню_зал")
inline_btn_poster = InlineKeyboardButton("Афиша", url='https://t.me/anekdot18')
inline_btn_subscription = InlineKeyboardButton("Проверить абонимент", callback_data="меню_абонимент")
inline_btn_price = InlineKeyboardButton("Цены", callback_data="меню_цены")
inline_btn_payment = InlineKeyboardButton("Купить абонимент", callback_data="меню_оплата")
inline_btn_hall_description = InlineKeyboardButton("Наши залы", callback_data="меню_залы")
inline_btn_contact = InlineKeyboardButton("О нас", callback_data="меню_котнакты")
inline_btn_registration = InlineKeyboardButton("Перерегестрироваться", callback_data="меню_регистрация")
inline_btn_enroll = InlineKeyboardButton("Записаться", url='https://mrqz.me/64d34a9c8c2025002566c344?mode=tg')

inline_kb_menu = InlineKeyboardMarkup(row_width=1)
inline_kb_menu.add(inline_btn_schedule).add(inline_btn_poster).add(inline_btn_subscription).add(inline_btn_price).\
    add(inline_btn_payment).add(inline_btn_contact).add(inline_btn_booking).add(inline_btn_hall_description).\
    add(inline_btn_enroll).add(inline_btn_registration).add(Inline_btn_finish)


inline_btn_bachata = InlineKeyboardButton("Бачата", callback_data="танец_бачата")
inline_btn_kizomba = InlineKeyboardButton("Кизомба", callback_data="танец_кизомба")

inline_dance_menu = InlineKeyboardMarkup(row_width=2)
inline_dance_menu.add(inline_btn_bachata, inline_btn_kizomba).add(Inline_btn_menu_back).add(Inline_btn_finish)


Inline_btn_small = InlineKeyboardButton("Стандартный абонемент на 8 занятий", callback_data="оплата_стандартный")
Inline_btn_medium = InlineKeyboardButton("Абонемент Max24/60", callback_data="оплата_средний")
Inline_btn_high = InlineKeyboardButton("Трехмесячный абонемент (24/90)", callback_data="оплата_большой")

inline_kb_payment = InlineKeyboardMarkup(row_width=3)
inline_kb_payment.add(Inline_btn_small).add(Inline_btn_medium).add(Inline_btn_high).add(Inline_btn_menu_back).\
    add(Inline_btn_finish)

inline_kb_term_of_usage = InlineKeyboardMarkup(row_width=2)
Inline_btn_small_term = InlineKeyboardButton("Менее 3-ех месяцев", callback_data="срок_мало")
Inline_btn_high_term = InlineKeyboardButton("Более 3-ех месяцев", callback_data="срок_много")
inline_kb_term_of_usage.add(Inline_btn_small_term).add(Inline_btn_high_term).add(Inline_btn_menu_back).\
    add(Inline_btn_finish)

inline_kb_subscription_exist = InlineKeyboardMarkup(row_width=2)
Inline_btn_small_term = InlineKeyboardButton("Да", callback_data="абонимент_да")
Inline_btn_high_term = InlineKeyboardButton("Нет", callback_data="абонимент_нет")
inline_kb_subscription_exist.add(Inline_btn_small_term).add(Inline_btn_high_term).add(Inline_btn_menu_back).\
    add(Inline_btn_finish)

inline_kb_free_hall = InlineKeyboardMarkup(row_width=3)
Inline_btn__first_hall = InlineKeyboardButton("Зал №1", url='https://calendar.yandex.by/embed/week?&layer_ids=24800608&tz_id=Europe/Minsk&layer_names=1 зал')
Inline_btn_second_hall = InlineKeyboardButton("Зал №2", url='https://calendar.yandex.by/embed/week?&layer_ids=24819666&tz_id=Europe/Minsk&layer_names=Зал №2')
Inline_btn_third_hall = InlineKeyboardButton("Зал №3", url='https://calendar.yandex.by/embed/week?&layer_ids=24819678&tz_id=Europe/Minsk&layer_names=Зал №3')
inline_kb_free_hall.add(Inline_btn__first_hall, Inline_btn_second_hall, Inline_btn_third_hall).\
    add(Inline_btn_menu_back).add(Inline_btn_finish)

inline_kb_cancel_registration = InlineKeyboardMarkup()
Inline_btn_cancel_registration = InlineKeyboardButton("Отменить регистрацию", callback_data="отмена_да")
inline_kb_cancel_registration.add(Inline_btn_cancel_registration)

inline_kb_halls = InlineKeyboardMarkup(row_width=3)
Inline_btn_one_hall = InlineKeyboardButton("Зал №1", callback_data="зал_первый")
Inline_btn_two_hall = InlineKeyboardButton("Зал №2", callback_data="зал_второй")
Inline_btn_three_hall = InlineKeyboardButton("Зал №3", callback_data="зал_третий")
inline_kb_halls.add(Inline_btn_one_hall, Inline_btn_two_hall, Inline_btn_three_hall).\
    add(Inline_btn_menu_back).add(Inline_btn_finish)
