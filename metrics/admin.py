from django.contrib import admin

from metrics.models import Access


class AccessAdmin(admin.ModelAdmin):
    list_display = ('id', 'ip', 'device', 'os', 'browser', 'qrcode')


admin.site.register(Access, AccessAdmin)
