from django.forms import ModelForm, Form, ChoiceField

from qr.models import QrCode, UrlQrCode, FileQrCode


class UrlQrCodeForm(ModelForm):
    class Meta:
        model = UrlQrCode
        fields = ['name', 'url']


class FileQrCodeForm(ModelForm):
    class Meta:
        model = FileQrCode
        fields = ['name', 'file']
