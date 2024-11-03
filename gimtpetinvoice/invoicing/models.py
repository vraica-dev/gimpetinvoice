from django.utils import timezone
from django.db import models
from provider.models import Provider
from django.db.models import Sum, F
from django.db.models.functions import Coalesce
from decimal import Decimal


class Invoice(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.DO_NOTHING, blank=False, null=False)
    total_amount = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    total_vat = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Invoice ID {self.pk}'

    def set_totals(self):
        totals = self.items.aggregate(
            total_amount=Coalesce(Sum('item_price_with_vat'), Decimal('0.00')),
            total_vat=Coalesce(Sum(F('item_price_with_vat') - F('item_price')), Decimal('0.00'))
            
        )
        self.total_amount = totals['total_amount']
        self.total_vat = totals['total_vat']

        self.save()


class InvoiceFragment(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, blank=False, null=False, related_name='items')
    product_name = models.CharField(max_length=30, null=False, blank=False, default="Generic Product")
    item_price = models.DecimalField(decimal_places=2, max_digits=10)
    item_price_with_vat = models.DecimalField(decimal_places=2, max_digits=10)
    vat = models.IntegerField(default=19)
    
    def __str__(self):
        return f'InvoiceFrag ID {self.pk} - Invoice ID {self.invoice.pk}'
