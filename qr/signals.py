from django.db.models.signals import post_save
from django.dispatch import receiver

from qr.models import QrCode, FileQrCode, URLQrCode, VideoQrCode


@receiver(post_save, sender=URLQrCode)
@receiver(post_save, sender=FileQrCode)
@receiver(post_save, sender=VideoQrCode)
def build_img_handler(sender, instance, created, raw, **kwargs):
    assert isinstance(instance, QrCode)
    if not hasattr(instance, '_build_save'):
        instance.build_image()
