# Generated by Django 2.1.8 on 2019-12-04 13:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0015_auto_20191126_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Nazwa'),
        ),
        migrations.AlterField(
            model_name='job',
            name='position_1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='first_position', to='employees.Position', verbose_name='stanowisko pierwsze'),
        ),
        migrations.AlterField(
            model_name='job',
            name='position_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='second_position', to='employees.Position', verbose_name='stanowisko drugie'),
        ),
        migrations.AlterField(
            model_name='job',
            name='size_of_position_1',
            field=models.DecimalField(decimal_places=2, max_digits=3, verbose_name='wielkość etatu na stanowisku 1'),
        ),
        migrations.AlterField(
            model_name='job',
            name='size_of_position_2',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True, verbose_name='wielkość etatu nastanowisku 2'),
        ),
        migrations.AlterField(
            model_name='manager',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.Job', verbose_name='praca'),
        ),
        migrations.AlterField(
            model_name='manager',
            name='work_place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.WorkPlace', verbose_name='miejsce pracy'),
        ),
        migrations.AlterField(
            model_name='position',
            name='description',
            field=models.CharField(blank=True, max_length=300, verbose_name='Opis'),
        ),
        migrations.AlterField(
            model_name='position',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Nazwa'),
        ),
        migrations.AlterField(
            model_name='supervisor',
            name='name',
            field=models.CharField(max_length=50, verbose_name='praca'),
        ),
        migrations.AlterField(
            model_name='supervisor',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='użytkownik'),
        ),
        migrations.AlterField(
            model_name='workplace',
            name='city',
            field=models.CharField(max_length=50, verbose_name='Miejscowość'),
        ),
        migrations.AlterField(
            model_name='workplace',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Nazwa'),
        ),
        migrations.AlterField(
            model_name='workplace',
            name='phone',
            field=models.CharField(max_length=13, verbose_name='Telefon'),
        ),
        migrations.AlterField(
            model_name='workplace',
            name='postal_code',
            field=models.CharField(max_length=8, verbose_name='Kod pocztowy'),
        ),
        migrations.AlterField(
            model_name='workplace',
            name='street',
            field=models.CharField(max_length=50, verbose_name='Ulica'),
        ),
    ]
