import asyncio

from celery import Celery

from database.database import async_session_maker
from database.database_manager import add_data_from_sheet_to_subscriptions, update_data_from_sheet_to_subscriptions

app = Celery('celery_app')
app.config_from_object('celeryconfig')


def run_async(func):
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(func)


@app.task
def add_data_to_subscriptions():
    result = run_async(add_data_from_sheet_to_subscriptions())
    return result


@app.task
def update_data_to_subscriptions():
    result = update_data_from_sheet_to_subscriptions()
    return result


app.log.setup(loglevel='DEBUG')
