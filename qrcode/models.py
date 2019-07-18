from django.db import models

from core.models import BasePolymorphicModel


class QrCode(BasePolymorphicModel):
    pass


class UrlQrCode(QrCode):
    url = models.URLField()


class FileQrCode(QrCode):
    file = models.FileField()
