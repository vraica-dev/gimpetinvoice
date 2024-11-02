from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=90, blank=False, null=False)
    county = models.CharField(max_length=90, blank=False, null=False)
    county_code = models.CharField(max_length=90, blank=False, null=False)

    class Meta:
        ordering = ['name']
        verbose_name = 'cities'

    def __str__(self):
        return str(self.name)
    

class Customer(models.Model):

    INVIDUAL = 'Individual'
    LEGAT_ENTITY = 'Legal Entity'

    CUSTOMER_TYPE = [
        (INVIDUAL, 'Individual'),
        (LEGAT_ENTITY, 'Legal Entity')
    ]

    first_name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=30, blank=False, null=False)
    customer_type = models.CharField(max_length=20, choices=CUSTOMER_TYPE, blank=False, null=False)
    ssn = models.CharField(max_length=17, blank=True, null=True)
    cif = models.CharField(max_length=17, blank=True, null=True)
    company_name = models.CharField(max_length=17, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING)
    street_name = models.CharField(max_length=17, blank=True, null=True)
    iban = models.CharField(max_length=30, blank=True, null=True)
    reg_number = models.CharField(max_length=17, blank=True, null=True)
    is_paying_tva = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name} | {self.customer_type}'





