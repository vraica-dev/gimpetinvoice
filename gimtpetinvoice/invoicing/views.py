from django.shortcuts import render
from .models import Invoice
from django.core.cache import caches
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest


def show_invoice(request, inv_id: int):
    if not request.user.is_authenticated:
        return HttpResponseBadRequest("User not loged in.")
    exiting_cache = caches['default'].get(f'{inv_id}_{request.user}')
    if exiting_cache:
        return exiting_cache
    else:
        invoice = Invoice.objects.get(id=inv_id)
        output = render(request, "invoice_display.html", {'invoice': invoice})
        caches['default'].set(f'{inv_id}_{request.user}', output, timeout=3)
        return output