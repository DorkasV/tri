# Generated by Django 2.1.5 on 2019-02-01 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('triathlon', '0022_auto_20190201_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='triathlon.City'),
        ),
    ]
