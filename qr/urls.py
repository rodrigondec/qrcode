from django.urls import path

from qr.views import ResolveQrCodeView, QrCodeListView, QrCodeCreateView, ChildQrCodeCreateView

urlpatterns = [
    path('qr/resolve/<pk>/', ResolveQrCodeView.as_view()),
    path('qr/lista/', QrCodeListView.as_view()),
    path('qr/cadastro/', QrCodeCreateView.as_view()),
    path('qr/cadastro/<qr_class>/', ChildQrCodeCreateView.as_view()),
]
