# Generated by Django 2.1.8 on 2019-07-18 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0005_clothe_prepared_to_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothe',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clothes_ordered', to='orders.Order'),
        ),
    ]