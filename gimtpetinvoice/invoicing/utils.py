import io
from xhtml2pdf import pisa
from django.http import HttpResponse
from html import escape
from django.template.loader import render_to_string

def render_html_to_pdf(template, ctx):
    html = render_to_string(template, ctx)
    result = io.BytesIO()

    pdf = pisa.pisaDocument(io.BytesIO(html.encode('utf-8')), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')