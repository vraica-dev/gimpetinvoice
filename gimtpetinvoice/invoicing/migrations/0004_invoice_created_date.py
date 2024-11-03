# Generated by Django 5.1.2 on 2024-11-03 10:28

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoicing', '0003_invoicefragment_product_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='created_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
