# Generated by Django 3.1.3 on 2023-07-05 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0031_auto_20230704_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='weight',
            field=models.IntegerField(default=None, null=True),
        ),
    ]
