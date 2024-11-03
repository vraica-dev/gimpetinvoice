from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from invoicing.models import Invoice
from invoicing.api.serializers import InvoiceSerializer


class InvoiceViewset(GenericViewSet, CreateModelMixin):
    permission_classes = [IsAuthenticated]
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)