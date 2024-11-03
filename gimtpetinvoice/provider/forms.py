from typing import Any
from django.forms import ModelForm
from django import forms
from provider.models import Provider


class ProviderForm(ModelForm):

    class Meta:
        model = Provider
        exclude = ['created_at', 'modified_at', 'provider_code']
        widgets = {
            'user': forms.HiddenInput()
        }