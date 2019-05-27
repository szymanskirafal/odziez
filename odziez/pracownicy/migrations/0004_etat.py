# Generated by Django 2.1.8 on 2019-05-27 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pracownicy', '0003_stanowisko'),
    ]

    operations = [
        migrations.CreateModel(
            name='Etat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wielkosc_etatu', models.DecimalField(decimal_places=2, max_digits=3)),
                ('miejsce_pracy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pracownicy', to='pracownicy.MiejscePracy')),
                ('stanowisko', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pracownicy', to='pracownicy.Stanowisko')),
            ],
        ),
    ]
