# Generated by Django 2.2.14 on 2020-12-03 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0028_auto_20201203_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='occupation',
            field=models.CharField(choices=[('Public Sector', 'Public Sector'), ('Private Sector', 'Private Sector'), ('Self-Employed', 'Self-Employed'), ('Unemployed', 'UnEmployed'), ('Student', 'Student')], default='M', max_length=100),
        ),
    ]