from django.urls import path
from django.contrib.auth import views as auth_views

from users.views import (PerfilView, MyLogoutView, MyPasswordChangeView,
                         MyPasswordResetView, MyPasswordResetConfirmView)


urlpatterns = [
    path('perfil/', PerfilView.as_view(), name='perfil'),

    path('login/', auth_views.LoginView.as_view(), name='entrar'),
    path('logout/', MyLogoutView.as_view(), name='sair'),

    path('mudar_senha/', MyPasswordChangeView.as_view(), name='mudar_senha'),

    path('resetar_senha/', MyPasswordResetView.as_view(), name='resetar_senha'),
    path('resetar/<uidb64>/<token>/', MyPasswordResetConfirmView.as_view(), name='resetar_senha_confirmar'),
]
