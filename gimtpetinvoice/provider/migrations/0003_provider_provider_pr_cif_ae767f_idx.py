# Generated by Django 5.1.2 on 2024-11-03 00:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0002_alter_provider_city'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddIndex(
            model_name='provider',
            index=models.Index(fields=['cif', 'user'], name='provider_pr_cif_ae767f_idx'),
        ),
    ]
