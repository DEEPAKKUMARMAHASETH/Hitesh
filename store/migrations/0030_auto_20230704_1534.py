# Generated by Django 3.1.3 on 2023-07-04 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0029_auto_20230625_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='weight',
            field=models.IntegerField(max_length=50),
        ),
    ]
