# Generated by Django 2.2.14 on 2020-12-01 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0018_product_offer_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='offer',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='offer_description',
            field=models.CharField(blank=True, default='', max_length=2000),
        ),
    ]
