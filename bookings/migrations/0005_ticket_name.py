# Generated by Django 2.2.14 on 2020-11-30 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0004_remove_ticket_product_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
