import os
from celery import Celery
from django.conf import settings

# Индикатор селери использует случайные настройки джанго
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project')

app = Celery('django_project')
app.config_from_object('django.conf:settings')
# эта линия говорит о селери о всех task.py в приложении
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)