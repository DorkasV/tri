# Generated by Django 2.1.5 on 2019-02-28 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('triathlon', '0054_remove_result_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='gender_place',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
