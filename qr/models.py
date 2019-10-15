from django.db import models
from django.conf import settings
from django.core.files.base import ContentFile

from core.models import BasePolymorphicModel
from core.mixins import PointModelMixin
from qr.utils import create_qrcode_io_stream, label_generator, get_qrcode_img_path,  get_file_path
from qr.constants import LABEL_SIZE


class QrCode(BasePolymorphicModel, PointModelMixin):
    label = models.CharField(unique=True, max_length=LABEL_SIZE*3, default=label_generator)
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

    @property
    def type(self):
        raise NotImplementedError('Must be called from a UrlQrCode or FileQrCode instance')

    @property
    def value(self):
        raise NotImplementedError('Must be called from a UrlQrCode or FileQrCode instance')


class URLQrCode(QrCode):
    url = models.URLField()

    @property
    def type(self):
        return 'URL'

    @property
    def value(self):
        return self.url


class VideoQrCode(URLQrCode):

    @property
    def type(self):
        return 'Video'


class FileQrCode(QrCode):
    file = models.FileField(upload_to=get_file_path)

    @property
    def type(self):
        return 'Arquivo'

    @property
    def value(self):
        return self.file.url
