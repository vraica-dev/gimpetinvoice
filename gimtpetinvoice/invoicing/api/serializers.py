from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers
from invoicing.models import InvoiceFragment, Invoice
from provider.models import Provider
from rest_framework.exceptions import ValidationError


class InvoiceFragmentSerializer(ModelSerializer):
    class Meta:
        model = InvoiceFragment
        fields = ['_all_']


class InvoiceSerializer(Serializer):
    provider_code = serializers.CharField(source='provider')
    total_amount = serializers.DecimalField(decimal_places=2, max_digits=4)
    total_vat = serializers.DecimalField(decimal_places=2, max_digits=4)

    def create(self, validated_data):
        provider_code = validated_data.pop("provider")
        try:
            provider = Provider.objects.get(provider_code=provider_code)
        except Provider.DoesNotExist:
            raise ValidationError("Provider not identified.")
        else:
            validated_data['provider'] = provider
            print(validated_data)
            invoice_instance = Invoice.objects.create(**validated_data)
            return invoice_instance
