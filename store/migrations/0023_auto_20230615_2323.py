# Generated by Django 3.1.3 on 2023-06-15 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0022_auto_20210124_0657'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=100)),
                ('age', models.IntegerField(blank=True, default=None, null=True)),
                ('gender', models.CharField(max_length=15)),
                ('phone', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('services', models.CharField(max_length=50)),
                ('slots', models.CharField(max_length=30)),
                ('weight', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
