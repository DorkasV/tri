# Generated by Django 2.1.5 on 2019-02-03 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('triathlon', '0034_result_xxx'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]