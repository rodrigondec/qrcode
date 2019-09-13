from django.forms import ModelForm

from qr.models import UrlQrCode, FileQrCode
from logos.forms import LogoChoiceField


class UrlQrCodeForm(ModelForm):
    logo = LogoChoiceField(required=False)

    class Meta:
        model = UrlQrCode
        fields = ['name', 'url']


class FileQrCodeForm(ModelForm):
    logo = LogoChoiceField(required=False)

    class Meta:
        model = FileQrCode
        fields = ['name', 'file']
