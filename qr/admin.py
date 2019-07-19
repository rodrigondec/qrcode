from django.contrib import admin
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin, PolymorphicChildModelFilter

from qr.models import QrCode, UrlQrCode, FileQrCode

BASE_DISPLAY_LIST = ['id', 'name', 'image']


@admin.register(UrlQrCode)
class ModelBAdmin(PolymorphicChildModelAdmin):
    base_model = UrlQrCode
    show_in_index = True
    list_display = BASE_DISPLAY_LIST + ['url']
    exclude = ['image']


@admin.register(FileQrCode)
class ModelCAdmin(PolymorphicChildModelAdmin):
    base_model = FileQrCode
    show_in_index = True
    list_display = BASE_DISPLAY_LIST + ['file']
    exclude = ['image']


@admin.register(QrCode)
class ModelAParentAdmin(PolymorphicParentModelAdmin):
    base_model = QrCode
    child_models = (UrlQrCode, FileQrCode)
    list_filter = (PolymorphicChildModelFilter,)
    list_display = BASE_DISPLAY_LIST
    exclude = ['image']
