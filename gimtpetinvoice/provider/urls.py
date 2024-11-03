from django.urls import path, include
from provider.views import ProviderView


urlpatterns = [
    path('add/', ProviderView.as_view())
]