from rest_framework.routers import DefaultRouter
from invoicing.api.views import InvoiceViewset
from django.urls import path, include
from .views import render_invoice_pdf


router = DefaultRouter()
router.register(r'invoices', InvoiceViewset, basename='invoice-viewset')

urlpatterns = [
    path('api/', include(router.urls)),
    path('render_inv/<int:inv_id>', render_invoice_pdf, name='render-pdf')
]