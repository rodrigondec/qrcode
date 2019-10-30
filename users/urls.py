from django.urls import path
from django.contrib.auth import views as auth_views

from users.views import MyPasswordChangeView, MyPasswordResetView, MyPasswordResetConfirmView


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('mudar_senha/', MyPasswordChangeView.as_view(), name='password_change'),

    path('resetar_senha/', MyPasswordResetView.as_view(), name='password_reset'),
    path('resetar/<uidb64>/<token>/', MyPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]
