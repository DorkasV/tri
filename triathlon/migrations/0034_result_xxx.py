# Generated by Django 2.1.5 on 2019-02-02 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('triathlon', '0033_result_zzz'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='xxx',
            field=models.DurationField(blank=True, null=True),
        ),
    ]