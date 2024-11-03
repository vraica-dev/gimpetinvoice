# Generated by Django 5.1.2 on 2024-11-03 00:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0005_provider_provider_code'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddIndex(
            model_name='provider',
            index=models.Index(fields=['provider_code'], name='provider_pr_provide_ecc01a_idx'),
        ),
    ]