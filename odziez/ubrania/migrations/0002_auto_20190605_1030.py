# Generated by Django 2.1.8 on 2019-06-05 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ubrania', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ubranie',
            name='pracownik',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ubrania', to='pracownicy.Pracownik'),
        ),
    ]