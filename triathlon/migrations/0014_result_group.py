# Generated by Django 2.1.5 on 2019-01-30 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('triathlon', '0013_result_distance'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='triathlon.Group'),
        ),
    ]
