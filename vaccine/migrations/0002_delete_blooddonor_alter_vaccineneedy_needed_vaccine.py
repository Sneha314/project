# Generated by Django 4.0.1 on 2022-01-19 05:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vaccine', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BloodDonor',
        ),
        migrations.AlterField(
            model_name='vaccineneedy',
            name='needed_vaccine',
            field=models.ForeignKey(default='covishield', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='vaccine.vaccines'),
        ),
    ]
