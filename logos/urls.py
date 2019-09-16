from django.urls import path

from logos.views import LogoListView, LogoCreateView, LogoUpdateView

urlpatterns = [
    path('logos/listar/', LogoListView.as_view()),
    path('logos/cadastrar/', LogoCreateView.as_view()),
    path('logos/atualizar/<pk>/', LogoUpdateView.as_view())
]
