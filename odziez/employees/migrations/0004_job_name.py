# Generated by Django 2.1.8 on 2019-11-25 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_auto_20191029_2037'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='name',
            field=models.CharField(default='aaa', max_length=150, verbose_name='name'),
            preserve_default=False,
        ),
    ]