# Generated by Django 5.1.1 on 2024-09-22 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_category_alter_service_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='duration',
            field=models.IntegerField(blank=True, help_text='Duration in minutes', null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='special_offer',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
