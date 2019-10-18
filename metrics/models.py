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

    qrcode = models.ForeignKey('qr.QrCode', on_delete=models.CASCADE)

    @classmethod
    def from_request(cls, qrcode, request, save=True):
        instance = cls()

        instance.ip = get_client_ip(request)

        user_agent = str(request.user_agent)
        instance.device = user_agent.split('/')[0]
        instance.os = user_agent.split('/')[1]
        instance.browser = user_agent.split('/')[2]

        instance.qrcode = qrcode

        instance.save()
        return instance

    @property
    def datetime(self):
        return pendulum.instance(self._datetime).in_tz('America/Sao_Paulo')
