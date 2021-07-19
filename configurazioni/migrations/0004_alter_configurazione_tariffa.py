# Generated by Django 3.2.4 on 2021-07-19 22:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tariffe', '0002_tariffa_prezzo'),
        ('configurazioni', '0003_alter_configurazione_tariffa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configurazione',
            name='tariffa',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tariffe.tariffa'),
            preserve_default=False,
        ),
    ]
