# Generated by Django 2.1.5 on 2019-02-04 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('triathlon', '0035_auto_20190203_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(max_length=10),
        ),
    ]
