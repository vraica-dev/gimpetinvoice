from django.shortcuts import render
from .models import Invoice
from .utils import render_html_to_pdf

# Create your views here.
def render_invoice_pdf(request, inv_id: int):
    invoice = Invoice.objects.get(id=inv_id)
    return render(request, "invoice_display.html", {'invoice': invoice})