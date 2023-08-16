import asyncio

from database.database import async_session_maker
from database.database_manager import add_data_from_sheet_to_subscriptions, update_data_from_sheet_to_subscriptions


async def run():
    await add_data_from_sheet_to_subscriptions()
    # await update_data_from_sheet_to_subscriptions(session)


if __name__ == '__main__':
    asyncio.run(run())
