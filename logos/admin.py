from django.contrib import admin

from logos.models import Logo


class LogoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image')


admin.site.register(Logo, LogoAdmin)
