from django.urls import path

from logos.views import LogoListView, LogoCreateView, LogoUpdateView

urlpatterns = [
    path('listar/', LogoListView.as_view()),
    path('cadastrar/', LogoCreateView.as_view()),
    path('atualizar/<pk>/', LogoUpdateView.as_view())
]
