from django.apps import AppConfig


class QrConfig(AppConfig):
    name = 'qr'

    # noinspection PyUnresolvedReferences
    def ready(self):
        import qr.signals
