# Generated by Django 2.1.8 on 2019-12-04 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0018_auto_20191204_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manufacturer',
            name='name',
            field=models.CharField(max_length=150, unique=True, verbose_name='Nazwa'),
        ),
    ]
