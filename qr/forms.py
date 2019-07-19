from django.forms import ModelForm, Form, ChoiceField

from qr.models import QrCode, UrlQrCode, FileQrCode


class QrCodeForm(Form):
    qr_class = ChoiceField(choices=((1, 'file'), (2, 'url')), label="", initial='', required=True)


class UrlQrCodeForm(ModelForm):
    class Meta:
        model = UrlQrCode
        exclude = ['img']


class FileQrCodeForm(ModelForm):
    class Meta:
        model = FileQrCode
        exclude = ['img']
