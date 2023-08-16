from datetime import datetime
from loguru import logger

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.database import async_session_maker
from models import User, Subscription
from load_data import get_sheet_data


async def save_user(session: AsyncSession, id: int, first_name: str, last_name: str, phone_number: str,
                    age: int, status: str):
    try:
        new_user = User(
            id=id,
            tg_first_name=first_name,
            tg_last_name=last_name,
            phone_number=phone_number,
            age=age,
            status=status)
        session.add(new_user)
        await session.commit()
    except Exception as e:
        print("Error saving user menu interaction:", e)


async def get_user_by_user_id(user_id):
    async with async_session_maker() as session:
        async with session.begin():
            user = await session.execute(select(User).filter(User.id == user_id))
            user = user.scalar()
        return user


async def get_user_by_phone_number(phone_number):
    async with async_session_maker() as session:
        async with session.begin():
            user = await session.execute(select(User).filter(User.phone_number == phone_number))
            user = user.scalar()
        return user


async def get_user_subscription(user_id):
    async with async_session_maker() as session:
        async with session.begin():
            subscription = await session.execute(select(Subscription).filter(Subscription.user_id == user_id))
            subscription = subscription.scalar_one_or_none()
        return subscription


async def delete_user_with_data(user_id):
    async with async_session_maker() as session:
        async with session.begin():

            await session.execute(Subscription.__table__.delete().where(Subscription.user_id == user_id))
            await session.execute(User.__table__.delete().where(User.id == user_id))

            await session.commit()


async def update_data_from_sheet_to_subscriptions():
    async with async_session_maker() as session:
        data = get_sheet_data('aboniments')
        for record in data:
            phone_number = str(record['Телефон'])
            user = await get_user_by_phone_number(phone_number)
            if user:
                try:
                    existing_subscription = await session.execute(
                        select(Subscription)
                        .where(Subscription.user_id == user.id)
                        .where(Subscription.date == datetime.strptime(record['Срока абонемента'], '%d.%m.%Y').date())
                    )

                    existing_subscription = existing_subscription.scalar()

                    if existing_subscription:
                        existing_subscription.visited_classes = record['Кол-во посещенных занятий']
                        existing_subscription.classes = record['Общее кол-во занятий']
                        existing_subscription.remaining_classes = record['Кол-во оставшихся дней']
                        existing_subscription.date = datetime.strptime(record['Срока абонемента'], '%d.%m.%Y').date()

                        await session.commit()
                except Exception as e:
                    logger.error("Error updating subscription: {}", e)


async def add_data_from_sheet_to_subscriptions():
    async with async_session_maker() as session:
        data = get_sheet_data('aboniments')
        for record in data:
            phone_number = str(record['Телефон'])
            user = await get_user_by_phone_number(phone_number)
            if user:
                try:
                    existing_subscription = await session.execute(
                        select(Subscription)
                        .where(Subscription.user_id == user.id)
                        .where(Subscription.date == datetime.strptime(record['Срока абонемента'], '%d.%m.%Y').date())
                    )

                    existing_subscription = existing_subscription.scalar()

                    if not existing_subscription:
                        subscription = Subscription(
                            visited_classes=record['Кол-во посещенных занятий'],
                            classes=record['Общее кол-во занятий'],
                            remaining_classes=record['Кол-во оставшихся дней'],
                            date=datetime.strptime(record['Срока абонемента'], '%d.%m.%Y').date(),
                            user_id=user.id
                        )

                        session.add(subscription)
                        await session.commit()
                except Exception as e:
                    logger.error("Error saving user menu interaction: {}", e)

