from django.contrib import admin
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin, PolymorphicChildModelFilter

from qr.models import QrCode, UrlQrCode, FileQrCode


@admin.register(UrlQrCode)
class ModelBAdmin(PolymorphicChildModelAdmin):
    base_model = UrlQrCode


@admin.register(FileQrCode)
class ModelCAdmin(PolymorphicChildModelAdmin):
    base_model = FileQrCode


@admin.register(QrCode)
class ModelAParentAdmin(PolymorphicParentModelAdmin):
    base_model = QrCode
    child_models = (UrlQrCode, FileQrCode)
    list_filter = (PolymorphicChildModelFilter,)
