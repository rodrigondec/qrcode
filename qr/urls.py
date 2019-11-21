from django.urls import path

from qr.views import QRCodeListView, QRCodeCreateView, QRCodeUpdateView

urlpatterns = [
    path('listar/', QRCodeListView.as_view(), name='qr_listar'),
    path('cadastrar/', QRCodeCreateView.as_view(), name='qr_cadastrar'),
    path('atualizar/<pk>/', QRCodeUpdateView.as_view(), name='qr_atualizar')
]
