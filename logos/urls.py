from django.urls import path

from logos.views import LogoListView, LogoCreateView, LogoUpdateView

urlpatterns = [
    path('listar/', LogoListView.as_view(), name='logos_listar'),
    path('cadastrar/', LogoCreateView.as_view(), name='logos_cadastrar'),
    path('atualizar/<pk>/', LogoUpdateView.as_view(), name='logos_atualizar')
]
