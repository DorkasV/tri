# Generated by Django 2.1.5 on 2019-02-11 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('triathlon', '0042_auto_20190204_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='athlete',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='result', to='triathlon.Athlete'),
        ),
        migrations.AlterField(
            model_name='result',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='result', to='triathlon.Event'),
        ),
    ]