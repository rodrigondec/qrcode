from django.urls import path

from qr.views import QRCodeListView, QRCodeCreateView, QRCodeUpdateView

urlpatterns = [
    path('listar/', QRCodeListView.as_view()),
    path('cadastrar/', QRCodeCreateView.as_view()),
    path('atualizar/<pk>/', QRCodeUpdateView.as_view())
]
