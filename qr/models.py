from django.db import models
from django.conf import settings
from django.core.files.base import ContentFile

from core.models import BasePolymorphicModel
from qr.utils import create_qrcode_io_stream, get_qrcode_img_path, get_file_path


class QrCode(BasePolymorphicModel):
    image = models.ImageField(upload_to=get_qrcode_img_path, null=True, blank=True)
    name = models.CharField(max_length=150)

    def build_image(self):
        self.image.save(self.data_name, ContentFile(create_qrcode_io_stream(self.data)))

    @property
    def data(self):
        return f'{settings.HOST_ADDRESS}/resolve/{self.id}'

    @property
    def data_name(self):
        return f'{self.id}'

    def resolve(self):
        raise NotImplementedError('Must be called from a UrlQrCode or FileQrCode instance')


class UrlQrCode(QrCode):
    url = models.URLField()

    def resolve(self):
        return self.url


class FileQrCode(QrCode):
    file = models.FileField(upload_to=get_file_path)

    @property
    def data_name(self):
        return self.file.name

    def resolve(self):
        return self.file.url
