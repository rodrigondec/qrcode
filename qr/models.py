from django.db import models
from django.core.files.base import ContentFile

from core.models import BasePolymorphicModel
from qr.utils import create_qrcode_io_stream, get_qrcode_img_path, get_file_path


class QrCode(BasePolymorphicModel):
    img = models.ImageField(upload_to=get_qrcode_img_path, null=True, blank=True)

    def build_img(self):
        self.img.save(self.data_name, ContentFile(create_qrcode_io_stream(self.data)))

    @property
    def data(self):
        raise NotImplementedError('Must be called from a UrlQrCode or FileQrCode instance')

    @property
    def data_name(self):
        raise NotImplementedError('Must be called from a UrlQrCode or FileQrCode instance')


class UrlQrCode(QrCode):
    url = models.URLField()

    @property
    def data(self):
        return self.url

    @property
    def data_name(self):
        return self.data


class FileQrCode(QrCode):
    file = models.FileField(upload_to=get_file_path)

    @property
    def data(self):
        return self.file.url

    @property
    def data_name(self):
        return self.file.name
