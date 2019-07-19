from django.db.models.signals import post_save
from django.dispatch import receiver

from qr.models import QrCode, FileQrCode, UrlQrCode


@receiver(post_save, sender=UrlQrCode)
@receiver(post_save, sender=FileQrCode)
def build_img_handler(sender, instance, created, raw, **kwargs):
    assert isinstance(instance, QrCode)
    if created:
        instance.build_image()
