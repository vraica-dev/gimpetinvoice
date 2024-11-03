from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers
from invoicing.models import InvoiceFragment, Invoice
from provider.models import Provider
from rest_framework.exceptions import ValidationError


class InvoiceFragmentSerializer(ModelSerializer):
    class Meta:
        model = InvoiceFragment
        fields = ['item_price', 'item_price_with_vat', 'vat']
    

class InvoiceSerializer(Serializer):
    provider_code = serializers.CharField(source='provider')
    items = InvoiceFragmentSerializer(many=True)


    def create(self, validated_data):
        provider_code = validated_data.pop("provider")
        items = validated_data.pop('items')
        
        try:
            provider = Provider.objects.get(provider_code=provider_code)
        except Provider.DoesNotExist:
            raise ValidationError("Provider not identified.")
        else:
            validated_data['provider'] = provider
            invoice_instance = Invoice.objects.create(**validated_data)
            
            # creating InvoiceFraments for the invoice
            for item in items:
                item_data = item
                item_data['invoice'] = invoice_instance
                InvoiceFragment.objects.create(**item_data)
            
            invoice_instance.set_totals()
            return invoice_instance
