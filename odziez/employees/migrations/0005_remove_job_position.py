# Generated by Django 2.1.8 on 2019-11-25 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0004_job_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='position',
        ),
    ]
