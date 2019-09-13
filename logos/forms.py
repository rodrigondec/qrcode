from django.forms import ModelChoiceField

from logos.models import Logo


class LogoChoiceField(ModelChoiceField):
    def __init__(self, *args, **kwargs):
        super().__init__(queryset=Logo.objects.all(), *args, **kwargs)

    def label_from_instance(self, obj):
        return obj.name
