import os
import redis
from celery.schedules import crontab

redis_url = os.environ.get('BROKER_URL')
redis_host = os.environ.get('BROKER_HOST')
redis_port = os.environ.get('BROKER_PORT')
redis_password = os.environ.get('BROKER_PASSWORD')

broker_url = redis_url
result_backend = redis_url
broker_connection_retry_on_startup = True

redis_client = redis.Redis(
    host=redis_host,
    port=redis_port,
    password=redis_password)

beat_schedule = {
    'add_data_from_sheet_to_subscriptions': {
        'task': 'celery_app.add_data_to_subscriptions',
        'schedule': crontab(hour='3')
    },

    'update_data_from_sheet_to_subscriptions': {
        'task': 'celery_app.update_data_to_subscriptions',
        'schedule': crontab(hour='3')
    },
}
