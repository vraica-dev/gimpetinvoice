from rest_framework.routers import DefaultRouter
from invoicing.api.views import InvoiceViewset
from django.urls import path, include
from .views import show_invoice


router = DefaultRouter()
router.register(r'invoices', InvoiceViewset, basename='invoice-viewset')

urlpatterns = [
    path(r'<version>/api/', include(router.urls)),
    path('show_invoice/<int:inv_id>', show_invoice, name='show-invoice')
]