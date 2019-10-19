import pendulum
from django.db import models

from core.models import BaseModel
from metrics.utils import get_client_ip


class Access(BaseModel):
    ip = models.GenericIPAddressField()

    _datetime = models.DateTimeField(default=pendulum.now)

    device = models.CharField(max_length=150)
    os = models.CharField(max_length=150)
    browser = models.CharField(max_length=150)

    qrcode = models.ForeignKey('qr.QrCode', related_name='access', on_delete=models.CASCADE)

    @classmethod
    def from_request(cls, qrcode, request, save=True):
        instance = cls()

        instance.ip = get_client_ip(request)

        user_agent = str(request.user_agent)
        instance.device = user_agent.split('/')[0].strip()
        instance.os = user_agent.split('/')[1].strip()
        instance.browser = user_agent.split('/')[2].strip()

        instance.qrcode = qrcode

        instance.save()
        return instance

    @property
    def datetime(self):
        return pendulum.instance(self._datetime).in_tz('America/Sao_Paulo')

    @classmethod
    def get_value_count(cls, attr_name):
        return cls.objects\
            .values(attr_name)\
            .annotate(models.Count(attr_name))

    @classmethod
    def get_formated_value_count(cls, attr_name):
        data = cls.get_value_count(attr_name)
        return [[item.get(attr_name), item.get(f'{attr_name}__count')] for item in data]

    @classmethod
    def get_timeline_count(cls):

        return cls.objects\
            .filter(_datetime__year=pendulum.now().year)\
            .values(
                '_datetime__year',
                '_datetime__month',
                '_datetime__day')\
            .annotate(models.Count('_datetime__day'))

    @classmethod
    def get_formated_timeline_count(cls):
        data = cls.get_timeline_count()
        return [
            [
                {
                    'year': item.get('_datetime__year'),
                    'month': item.get('_datetime__month'),
                    'day': item.get('_datetime__day'),
                },
                item.get('_datetime__day__count')
            ]
            for item in data
        ]
