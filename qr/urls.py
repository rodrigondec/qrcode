from django.urls import path

from qr.views import ResolveQrCodeView, QRCodeListView, QRCodeCreateView, QRCodeUpdateView

urlpatterns = [
    path('qr/resolve/<pk>/', ResolveQrCodeView.as_view()),
    path('qr/listar/', QRCodeListView.as_view()),
    path('qr/cadastrar/', QRCodeCreateView.as_view()),
    path('qr/atualizar/<pk>/', QRCodeUpdateView.as_view())
]
