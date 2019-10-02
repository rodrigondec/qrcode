from django.db import models
from django.conf import settings
from django.core.files.base import ContentFile

from core.models import BasePolymorphicModel
from qr.utils import create_qrcode_io_stream, get_qrcode_img_path,  get_file_path


class QrCode(BasePolymorphicModel):
    image = models.ImageField(upload_to=get_qrcode_img_path, null=True, blank=True)
    name = models.CharField(max_length=150)
    logo = models.ForeignKey('logos.Logo', on_delete=models.SET_NULL, null=True, blank=True)

    def build_image(self):
        self.image.save(self.data_name, ContentFile(create_qrcode_io_stream(self.data, self.logo)), save=False)
        self._build_save = True
        self.save()

    @property
    def data(self):
        return f'{settings.HOST_ADDRESS}/qr/resolve/{self.id}'

    @property
    def data_name(self):
        return f'{self.id}'

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
    def data_name(self):
        return self.file.name

    @property
    def type(self):
        return 'Arquivo'

    @property
    def value(self):
        return self.file.url
