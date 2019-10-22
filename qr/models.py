from django.db import models
from django.conf import settings
from django.core.files.base import ContentFile

import json

from core.models import BasePolymorphicModel
from core.mixins import PointModelMixin
from qr.utils import create_qrcode_io_stream, label_generator, get_qrcode_img_path,  get_file_path
from qr.constants import (QR_LABEL_SIZE, LEAFLET_ICON, LEAFLET_SHAPE,
                          LEAFLET_BACKGROUND_COLOR)
from qr.leaflet import LeafletColorManager


class QrCode(BasePolymorphicModel, PointModelMixin):
    label = models.CharField(unique=True, max_length=QR_LABEL_SIZE * 3, default=label_generator)
    image = models.ImageField(upload_to=get_qrcode_img_path, null=True, blank=True)
    name = models.CharField(max_length=150)
    logo = models.ForeignKey('logos.Logo', on_delete=models.SET_NULL, null=True, blank=True)

    def build_image(self):
        self.image.save(None, ContentFile(create_qrcode_io_stream(self.resolve_url, self.logo)), save=False)
        self._build_save = True
        self.save()

    @property
    def resolve_url(self):
        return f'{settings.HOST_ADDRESS}/ver_qr/{self.label}'

    @staticmethod
    def resolve_template():
        raise NotImplementedError('Não pode ser chamado direto de um QrCode!')

    @property
    def type(self):
        raise NotImplementedError('Não pode ser chamado direto de um QrCode!')

    @property
    def value(self):
        raise NotImplementedError('Não pode ser chamado direto de um QrCode!')

    @property
    def leaflet_options(self):
        color = LeafletColorManager.pick(self.access.count())
        options = {
            "icon": LEAFLET_ICON,
            "iconShape": LEAFLET_SHAPE,
            "borderColor": color,
            "textColor": color,
            "backgroundColor": LEAFLET_BACKGROUND_COLOR,
        }
        return json.dumps(options)

    @property
    def leaflet_title(self):
        return f"Esse QR Code teve { self.access.count() } acessos!"


class URLQrCode(QrCode):
    url = models.URLField()

    @property
    def type(self):
        return 'URL'

    @property
    def value(self):
        return self.url

    @staticmethod
    def resolve_template():
        return 'qr/resolve/url.html'


class VideoQrCode(URLQrCode):

    @property
    def type(self):
        return 'Video'

    @staticmethod
    def resolve_template():
        return 'qr/resolve/video.html'


class FileQrCode(QrCode):
    file = models.FileField(upload_to=get_file_path)

    @property
    def type(self):
        return 'Arquivo'

    @property
    def value(self):
        return self.file.url

    @staticmethod
    def resolve_template():
        return 'qr/resolve/arquivo.html'

    @property
    def file_url(self):
        return f'{settings.HOST_ADDRESS}{self.value}'
