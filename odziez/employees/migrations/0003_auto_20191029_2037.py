# Generated by Django 2.1.8 on 2019-10-29 20:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_auto_20190709_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='body_size',
            field=models.CharField(choices=[('XL', 'XL'), ('L', 'L'), ('M', 'M'), ('S', 'S')], max_length=2, verbose_name='body_size'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='colar',
            field=models.PositiveSmallIntegerField(verbose_name='colar'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='height',
            field=models.PositiveSmallIntegerField(verbose_name='height'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.Job', verbose_name='job'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(max_length=15, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='sex',
            field=models.CharField(choices=[('W', 'Kobieta'), ('M', 'Mężczyzna')], max_length=1, verbose_name='sex'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='shoe_size',
            field=models.PositiveSmallIntegerField(verbose_name='shoe_size'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='surname',
            field=models.CharField(max_length=40, verbose_name='surname'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='width_waist',
            field=models.PositiveSmallIntegerField(verbose_name='width_waist'),
        ),
        migrations.AlterField(
            model_name='job',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.Position', verbose_name='position'),
        ),
        migrations.AlterField(
            model_name='job',
            name='size_of_job',
            field=models.DecimalField(decimal_places=2, max_digits=3, verbose_name='size_of_job'),
        ),
        migrations.AlterField(
            model_name='job',
            name='work_place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.WorkPlace', verbose_name='work_place'),
        ),
        migrations.AlterField(
            model_name='manager',
            name='body_size',
            field=models.CharField(choices=[('XL', 'XL'), ('L', 'L'), ('M', 'M'), ('S', 'S')], max_length=2, verbose_name='body_size'),
        ),
        migrations.AlterField(
            model_name='manager',
            name='colar',
            field=models.PositiveSmallIntegerField(verbose_name='colar'),
        ),
        migrations.AlterField(
            model_name='manager',
            name='height',
            field=models.PositiveSmallIntegerField(verbose_name='height'),
        ),
        migrations.AlterField(
            model_name='manager',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.Job', verbose_name='job'),
        ),
        migrations.AlterField(
            model_name='manager',
            name='name',
            field=models.CharField(max_length=15, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='manager',
            name='sex',
            field=models.CharField(choices=[('W', 'Kobieta'), ('M', 'Mężczyzna')], max_length=1, verbose_name='sex'),
        ),
        migrations.AlterField(
            model_name='manager',
            name='shoe_size',
            field=models.PositiveSmallIntegerField(verbose_name='shoe_size'),
        ),
        migrations.AlterField(
            model_name='manager',
            name='surname',
            field=models.CharField(max_length=40, verbose_name='surname'),
        ),
        migrations.AlterField(
            model_name='manager',
            name='width_waist',
            field=models.PositiveSmallIntegerField(verbose_name='width_waist'),
        ),
        migrations.AlterField(
            model_name='position',
            name='description',
            field=models.CharField(max_length=300, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='position',
            name='name',
            field=models.CharField(max_length=150, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='supervisor',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='supervisor',
            name='name',
            field=models.CharField(max_length=50, verbose_name='job'),
        ),
        migrations.AlterField(
            model_name='supervisor',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='job'),
        ),
        migrations.AlterField(
            model_name='workplace',
            name='city',
            field=models.CharField(max_length=50, verbose_name='city'),
        ),
        migrations.AlterField(
            model_name='workplace',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='workplace',
            name='name',
            field=models.CharField(max_length=150, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='workplace',
            name='phone',
            field=models.CharField(max_length=13, verbose_name='phone'),
        ),
        migrations.AlterField(
            model_name='workplace',
            name='postal_code',
            field=models.CharField(max_length=8, verbose_name='postal_code'),
        ),
        migrations.AlterField(
            model_name='workplace',
            name='street',
            field=models.CharField(max_length=50, verbose_name='street'),
        ),
    ]
