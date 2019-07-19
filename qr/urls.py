from django.urls import path

from qr.views import GetQrCodeView

urlpatterns = [
    path('resolve/<pk>/', GetQrCodeView.as_view())
]
