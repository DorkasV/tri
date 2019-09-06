# Generated by Django 2.1.5 on 2019-02-28 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('triathlon', '0048_athlete_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='athlete',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='test', to='triathlon.Athlete'),
        ),
        migrations.AddField(
            model_name='test',
            name='distance',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='triathlon.Distance'),
        ),
        migrations.AddField(
            model_name='test',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='test', to='triathlon.Event'),
        ),
        migrations.AddField(
            model_name='test',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='triathlon.Group'),
        ),
    ]
