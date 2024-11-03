from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.permissions import IsAuthenticated
from invoicing.models import Invoice
from invoicing.api.serializers import InvoiceSerializer
from rest_framework.response import Response
from provider.models import Provider
from .helpers import InvoicePaginator


class InvoiceViewset(GenericViewSet, CreateModelMixin, ListModelMixin):
    permission_classes = [IsAuthenticated]
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    pagination_class = InvoicePaginator
    
    def create(self, request, *args, **kwargs):
        serz = self.get_serializer_class()
        serializer = serz(data=request.data)

        if serializer.is_valid(raise_exception=True):
            instance = serializer.save()
            return Response(data={"id": instance.id})
        
    def list(self, request, *args, **kwargs):
        """
        paginated listing of the invoices by provider
        """
        serializer = self.get_serializer_class()
        user = self.request.user

        provider = Provider.objects.filter(user=user)
        qset = self.get_queryset().filter(provider__in=provider).order_by('total_amount')

        paginator = InvoicePaginator()
        page = paginator.paginate_queryset(qset, request)
        if page:
            ser = serializer(page, many=True)
            return paginator.get_paginated_response(ser.data)
        
        return Response( serializer(qset, many=True).data)