from django.urls import path, include
from provider.views import ProviderCreateView, ProviderProfileView


urlpatterns = [
    path('add/', ProviderCreateView.as_view()),
    path('profile/', ProviderProfileView.as_view())
]