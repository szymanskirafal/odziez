# Generated by Django 2.1.8 on 2019-07-27 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0012_clothe_delivered_with_defects'),
    ]

    operations = [
        migrations.AddField(
            model_name='clothe',
            name='not_delivered',
            field=models.BooleanField(default=False),
        ),
    ]