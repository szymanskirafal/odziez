# Generated by Django 2.1.8 on 2019-07-06 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employees', '0001_initial'),
        ('clothes', '0001_initial'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kindofclothe',
            name='available_for',
            field=models.ManyToManyField(to='employees.Position'),
        ),
        migrations.AddField(
            model_name='clothe',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clothes', to='employees.Employee'),
        ),
        migrations.AddField(
            model_name='clothe',
            name='kind',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chosen', to='clothes.KindOfClothe'),
        ),
        migrations.AddField(
            model_name='clothe',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Order'),
        ),
    ]
