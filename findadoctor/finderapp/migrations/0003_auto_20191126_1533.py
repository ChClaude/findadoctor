# Generated by Django 2.2.7 on 2019-11-26 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finderapp', '0002_auto_20191126_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date',
            field=models.DateTimeField(verbose_name='Date and Time Booked'),
        ),
    ]