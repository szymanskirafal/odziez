# Generated by Django 2.1.8 on 2019-07-10 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0002_auto_20190709_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothe',
            name='ordered',
            field=models.DateField(blank=True, null=True),
        ),
    ]