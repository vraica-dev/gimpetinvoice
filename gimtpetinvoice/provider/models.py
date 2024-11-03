from django.db import models
from django.contrib.auth.models import User


class City(models.Model):
    name = models.CharField(max_length=90, blank=False, null=False)
    county = models.CharField(max_length=90, blank=False, null=False)
    county_code = models.CharField(max_length=90, blank=False, null=False)

    class Meta:
        ordering = ['name']
        verbose_name = 'cities'

    def __str__(self):
        return str(self.name)
    

class Provider(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=50, blank=False, null=False)
    cif = models.CharField(max_length=15, blank=False, null=False, unique=True)
    reg_number = models.CharField(max_length=15, blank=False, null=False, unique=True)
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING, blank=False, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    bank_acc = models.CharField(max_length=25, blank=False, null=False)
    bank = models.CharField(max_length=55, blank=False, null=False)
    social_cap = models.FloatField(blank=False, null=False, default=200.0)
    provider_code = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [models.Index(fields=['cif', 'user']), models.Index(fields=['provider_code'])]

    def __str__(self):
        return f'{self.name} - {self.cif}'
    

    def save(self, *args, **kwargs):
        self.provider_code = f'{str(self.name[:3]).strip()}{str(self.reg_number[:2]).strip()}__GPI'
        super(Provider, self).save(*args, **kwargs)
    
    