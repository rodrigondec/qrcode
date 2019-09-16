from django.forms import ModelForm

from qr.models import URLQrCode, FileQrCode
from logos.forms import LogoChoiceField


class URLQrCodeForm(ModelForm):
    logo = LogoChoiceField(required=False)

    class Meta:
        model = URLQrCode
        fields = ['name', 'url', 'logo']


class FileQrCodeForm(ModelForm):
    logo = LogoChoiceField(required=False)

    class Meta:
        model = FileQrCode
        fields = ['name', 'file', 'logo']
