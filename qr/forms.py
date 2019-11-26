from django.forms import ModelForm, ChoiceField, HiddenInput
from crispy_forms.helper import FormHelper


from qr.models import URLQrCode, FileQrCode, VideoQrCode
from logos.forms import LogoChoiceField


CHOICES = [
    (URLQrCode.type(), URLQrCode.type()),
    (VideoQrCode.type(), VideoQrCode.type()),
    (FileQrCode.type(), FileQrCode.type())
]


class URLQrCodeForm(ModelForm):
    logo = LogoChoiceField(required=False)
    type = ChoiceField(choices=CHOICES, widget=HiddenInput(), initial=URLQrCode.type())

    class Meta:
        model = URLQrCode
        fields = ['name', 'url', 'logo', 'latitude', 'longitude']

    def __init__(self, *args, **kwargs):
        super(URLQrCodeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()


class VideoQrCodeForm(ModelForm):
    logo = LogoChoiceField(required=False)
    type = ChoiceField(choices=CHOICES, widget=HiddenInput(), initial=VideoQrCode.type())

    class Meta:
        model = VideoQrCode
        fields = ['name', 'url', 'logo', 'latitude', 'longitude']

    def __init__(self, *args, **kwargs):
        super(VideoQrCodeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()


class FileQrCodeForm(ModelForm):
    logo = LogoChoiceField(required=False)
    type = ChoiceField(choices=CHOICES, widget=HiddenInput(), initial=FileQrCode.type())

    class Meta:
        model = FileQrCode
        fields = ['name', 'file', 'logo', 'latitude', 'longitude']

    def __init__(self, *args, **kwargs):
        super(FileQrCodeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()


FORM_CLASSES = {
    f'{URLQrCode.type()}': URLQrCodeForm,
    f'{VideoQrCode.type()}': VideoQrCodeForm,
    f'{FileQrCode.type()}': FileQrCodeForm
}
