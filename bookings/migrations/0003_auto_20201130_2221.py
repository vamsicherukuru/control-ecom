# Generated by Django 2.2.14 on 2020-11-30 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_ticket_column'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='column',
        ),
        migrations.AddField(
            model_name='ticket',
            name='Product_code',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], default='', max_length=100),
        ),
    ]
