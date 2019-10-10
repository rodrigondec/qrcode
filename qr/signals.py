from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from qr.models import QrCode, FileQrCode, URLQrCode, VideoQrCode
from qr.utils import label_generator


@receiver(post_save, sender=URLQrCode)
@receiver(post_save, sender=FileQrCode)
@receiver(post_save, sender=VideoQrCode)
def build_img_handler(sender, instance, created, raw, **kwargs):
    assert isinstance(instance, QrCode)
    if not hasattr(instance, '_build_save'):
        instance.build_image()


@receiver(pre_save, sender=URLQrCode)
@receiver(pre_save, sender=FileQrCode)
@receiver(pre_save, sender=VideoQrCode)
def verify_unique_label(sender, instance, raw, **kwargs):
    assert isinstance(instance, QrCode)
    if instance.pk is None:
        while QrCode.objects.filter(label=instance.label):
            instance.label = label_generator()
