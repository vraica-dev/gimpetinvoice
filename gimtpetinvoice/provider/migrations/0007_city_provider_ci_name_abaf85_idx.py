# Generated by Django 5.1.2 on 2024-11-03 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0006_provider_provider_pr_provide_ecc01a_idx'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='city',
            index=models.Index(fields=['name'], name='provider_ci_name_abaf85_idx'),
        ),
    ]