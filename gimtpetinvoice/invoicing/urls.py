from rest_framework.routers import DefaultRouter
from invoicing.api.views import InvoiceViewset
from django.urls import path, include


router = DefaultRouter()
router.register(r'invoices', InvoiceViewset, basename='invoice-viewset')

urlpatterns = [
    path('api/', include(router.urls))
]