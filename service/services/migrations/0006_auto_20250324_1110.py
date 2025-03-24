# Generated by Django 3.2.16 on 2025-03-24 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_subscription_services_su_price_ea0e35_idx'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='subscription',
            name='services_su_price_ea0e35_idx',
        ),
        migrations.AddIndex(
            model_name='subscription',
            index=models.Index(fields=['price', 'plan'], name='services_su_price_cfea9e_idx'),
        ),
    ]
