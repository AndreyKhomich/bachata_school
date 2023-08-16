from aiogram.types import CallbackQuery

from keyboards import inline_kb_cancel_registration

from aiogram.dispatcher.filters.state import State, StatesGroup

from aiogram.dispatcher import FSMContext
from database.database import async_session_maker
from keyboards import inline_kb_menu
from aiogram import types
from database.database_manager import save_user, get_user_by_user_id
from src.create_bot import bot


class AuthStates(StatesGroup):
    waiting_for_first_name = State()
    waiting_for_last_name = State()
    waiting_for_age = State()
    waiting_for_phone_number = State()


async def start(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    user = await get_user_by_user_id(user_id)

    if user:
        await message.reply(" Пожалуйста используйте меню для взаимодействия с ботом.",
                            reply_markup=inline_kb_menu
                            )
        await state.set_state('menu_option')
    else:
        await message.reply("Добро пожаловать в нашу танцевальную школу!\n\n"
                            "Для начала работы пожалуйста зарегестрируйтесь. Введите ваше имя")
        await AuthStates.waiting_for_first_name.set()


async def process_first_name(message: types.Message, state: FSMContext):
    first_name = message.text
    await state.update_data(first_name=first_name)
    await message.reply(f"Введите вашу фамилию:",
                        reply_markup=inline_kb_cancel_registration)
    await AuthStates.waiting_for_last_name.set()


async def process_last_name(message: types.Message, state: FSMContext):
    last_name = message.text
    await state.update_data(last_name=last_name)

    await AuthStates.waiting_for_age.set()
    await message.reply("Отлично! Укажите ваш возраст (18 - 150):",
                        reply_markup=inline_kb_cancel_registration)


async def process_age(message: types.Message, state: FSMContext):
    age = message.text
    if age.isnumeric() and 150 > int(age) > 18:
        await state.update_data(age=age)

        await AuthStates.waiting_for_phone_number.set()
        await message.reply("Супер! Введите ваш номер телефона (например: 37544111111):",
                            reply_markup=inline_kb_cancel_registration)
    else:
        await message.answer(text="Введите возраст в диапазоне от 18 до 150 лет",
                             reply_markup=inline_kb_cancel_registration)


async def process_user_data(message: types.Message, state: FSMContext):
    phone_number = message.text
    if phone_number.isnumeric() and len(phone_number) == 12:
        await state.update_data(phone_number=phone_number)

        user_id = message.from_user.id
        user_data = await state.get_data()
        first_name = user_data.get("first_name")
        last_name = user_data.get("last_name")
        age = user_data.get("age")

        response = (
            f"{first_name} {last_name}, спасибо за предоставленную информацию!\n"
            f"Номер вашего телефона: {phone_number}\n"
            f" Ваш возраст: {age}\n"
            f"Все функции бота для вас доступны. Пожалуйста используйте меню:"

        )

        async with async_session_maker() as session:
            await save_user(session, user_id, first_name, last_name, phone_number, age, status='created')

        await message.reply(response, reply_markup=inline_kb_menu)
        await state.set_state('menu_option')

    else:
        await message.answer(text="Введите корректный номер телефона")


async def cancel_registration(callback_query: CallbackQuery, state: FSMContext):
    selected_option = callback_query.data.split('_')[1]
    chat_id = callback_query.from_user.id

    if selected_option == 'да':
        await bot.send_message(chat_id=chat_id,
                               text="Регистрация успешно отменена. Вы можете начать регистрацию повторно /start.",
                               )
        await state.finish()
    await callback_query.answer()
