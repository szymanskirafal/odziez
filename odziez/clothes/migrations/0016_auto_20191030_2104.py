# Generated by Django 2.1.8 on 2019-10-30 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0015_auto_20191029_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manufacturer',
            name='name',
            field=models.CharField(max_length=150, unique=True, verbose_name='Nazwa Producetna'),
        ),
    ]