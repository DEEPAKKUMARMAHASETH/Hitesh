# Generated by Django 3.1.3 on 2021-01-06 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_auto_20210105_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='logo',
            field=models.ImageField(default='', upload_to='static'),
        ),
    ]