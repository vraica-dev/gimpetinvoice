from django.db import models
from django.db.models import fields

# Create your models here.
class City(models.Model):
    name = fields.CharField(max_length=90, blank=False, null=False)
    county = fields.CharField(max_length=90, blank=False, null=False)
    county_code = fields.CharField(max_length=90, blank=False, null=False)

    class Meta:
        ordering = ['name']
        verbose_name = 'cities'

    def __str__(self):
        return str(self.name)