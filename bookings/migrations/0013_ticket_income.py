# Generated by Django 2.2.14 on 2020-12-01 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0012_userprofile_income'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='income',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
