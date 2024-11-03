from django.urls import path, include
from provider.views import ProviderCreateView, ProviderProfileView
from rest_framework.authtoken import views
from provider.api.views import ListProviders


urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('add/', ProviderCreateView.as_view()),
    path('profile/', ProviderProfileView.as_view()),
    path('<version>/list-providers/', ListProviders.as_view())
    
]