# Generated by Django 2.1.8 on 2019-11-26 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0008_auto_20191126_0706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='position_1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='first_position', to='employees.Position', verbose_name='position_1'),
        ),
        migrations.AlterField(
            model_name='job',
            name='position_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='second_position', to='employees.Position', verbose_name='position_2'),
        ),
        migrations.AlterField(
            model_name='job',
            name='size_of_position_1',
            field=models.DecimalField(decimal_places=2, max_digits=3, verbose_name='size_of_job_1'),
        ),
        migrations.AlterField(
            model_name='job',
            name='size_of_position_2',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True, verbose_name='size_of_job_2'),
        ),
    ]