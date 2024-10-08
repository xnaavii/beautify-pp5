# Generated by Django 5.1.1 on 2024-09-22 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='guest_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='guest_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
