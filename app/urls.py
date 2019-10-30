"""QrCode URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from core.urls import urlpatterns as core_urls
from qr.urls import urlpatterns as qr_urls
from logos.urls import urlpatterns as logos_urls
from users.urls import urlpatterns as users_urls
from qr.views import ResolveQrCodeView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(core_urls)),
    path('ver_qr/<id>/', ResolveQrCodeView.as_view()),
    path('qr/', include(qr_urls)),
    path('logos/', include(logos_urls)),
    path('accounts/', include(users_urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
