from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')


app = Celery('config', broker='redis://13.48.71.127:6379/9')


app.config_from_object('django.conf:settings', namespace='CELERY')


app.autodiscover_tasks()






