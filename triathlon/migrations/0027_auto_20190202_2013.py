# Generated by Django 2.1.5 on 2019-02-02 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('triathlon', '0026_auto_20190202_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='city', to='triathlon.Country'),
        ),
    ]