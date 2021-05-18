# Generated by Django 2.2.14 on 2020-11-30 16:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('card_number', models.IntegerField(default='')),
                ('cvv', models.IntegerField(default='')),
                ('CardHolder_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('poster', models.ImageField(blank=True, upload_to='movie_posters')),
                ('description', models.CharField(default='', max_length=1000)),
                ('basic_price', models.IntegerField(default=100)),
                ('Type', models.CharField(choices=[('Suitcase', 'Suitcase'), ('Straws', 'Straws'), ('Plates', 'Plates')], default='', max_length=100)),
                ('column_number', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Location', models.CharField(default='', max_length=100)),
                ('balance', models.IntegerField(default=500)),
                ('age', models.IntegerField(default='')),
                ('mobilenumber', models.IntegerField(default='')),
                ('gender', models.CharField(default='M', max_length=1)),
                ('address', models.TextField(default=' ', max_length=1000)),
                ('profilePic', models.ImageField(blank=True, upload_to='profile_pics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookings.Product')),
            ],
        ),
    ]