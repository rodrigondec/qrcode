from django.contrib import admin
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin, PolymorphicChildModelFilter

from qr.models import QrCode, URLQrCode, FileQrCode, VideoQrCode

BASE_DISPLAY_LIST = ['id', 'name', 'image']


@admin.register(URLQrCode)
class URLAdmin(PolymorphicChildModelAdmin):
    base_model = URLQrCode
    show_in_index = True
    list_display = BASE_DISPLAY_LIST + ['url']


@admin.register(VideoQrCode)
class VideoAdmin(PolymorphicChildModelAdmin):
    base_model = VideoQrCode
    show_in_index = True
    list_display = BASE_DISPLAY_LIST + ['url']


@admin.register(FileQrCode)
class FileAdmin(PolymorphicChildModelAdmin):
    base_model = FileQrCode
    show_in_index = True
    list_display = BASE_DISPLAY_LIST + ['file']


@admin.register(QrCode)
class QrCodeAdmin(PolymorphicParentModelAdmin):
    base_model = QrCode
    child_models = (URLQrCode, FileQrCode)
    list_filter = (PolymorphicChildModelFilter,)
    list_display = BASE_DISPLAY_LIST
