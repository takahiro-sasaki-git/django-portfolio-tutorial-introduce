# Generated by Django 3.1.11 on 2021-06-01 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_work'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='url',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='URL'),
        ),
    ]
