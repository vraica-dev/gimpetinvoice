from django.contrib import admin
from provider.models import City, Provider
from invoicing.models import InvoiceFragment, Invoice

admin.site.register(City)
admin.site.register(Provider)

admin.site.register(Invoice)
admin.site.register(InvoiceFragment)