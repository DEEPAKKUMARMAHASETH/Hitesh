# Generated by Django 3.1.3 on 2021-01-23 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_auto_20210123_1240'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sale_price',
            field=models.CharField(default=0, max_length=10),
        ),
        migrations.AddField(
            model_name='product',
            name='save',
            field=models.IntegerField(default=0),
        ),
    ]
