from django.db import models
from provider.models import Provider


class Invoice(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.DO_NOTHING, blank=False, null=False)
    total_amount = models.DecimalField(decimal_places=2, max_digits=4)
    total_vat = models.DecimalField(decimal_places=2, max_digits=4)

class InvoiceFragment(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.DO_NOTHING, blank=False, null=False)
    item_price = models.DecimalField(decimal_places=2, max_digits=4)
    item_price_with_vat = models.DecimalField(decimal_places=2, max_digits=4)
    vat = models.IntegerField(default=19)
