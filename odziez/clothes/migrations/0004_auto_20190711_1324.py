# Generated by Django 2.1.8 on 2019-07-11 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0003_auto_20190710_2108'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kindofclothe',
            old_name='time_to_exchange',
            new_name='months_to_exchange',
        ),
    ]
