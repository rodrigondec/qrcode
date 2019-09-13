from django.urls import path

from logos.views import LogoListView

urlpatterns = [
    path('logo/lista/', LogoListView.as_view()),
]
