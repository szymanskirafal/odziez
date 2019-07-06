# Generated by Django 2.1.8 on 2019-07-06 12:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employees', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='supervisor',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='job',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.Position'),
        ),
        migrations.AddField(
            model_name='job',
            name='work_place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.WorkPlace'),
        ),
        migrations.AddField(
            model_name='employee',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.Job'),
        ),
        migrations.AddField(
            model_name='manager',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
