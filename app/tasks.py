import requests
from bs4 import BeautifulSoup
from celery import shared_task
from celery.utils.log import get_task_logger
from django.db import transaction

import app.models as models

logger = get_task_logger(__name__)


@shared_task
def parsing_fact():
    with transaction.atomic():
        try:
            url = 'https://randstuff.ru/fact/'
            response = requests.get(url)
            if response.status_code == 200:
                content = BeautifulSoup(response.content, features='html.parser').find('td')
                checking = models.Fact.objects.filter(fact_title=content.text)
                if not checking:
                    models.Fact.objects.create(fact_title=content.text)
                return True
            else:
                return False
        except Exception as e:
            print(f"Error happened: {e}")
            return False
