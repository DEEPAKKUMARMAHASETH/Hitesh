# Generated by Django 3.1.3 on 2023-06-24 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0026_auto_20230616_1250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='modalities',
        ),
        migrations.RemoveField(
            model_name='users',
            name='services',
        ),
    ]
