# Generated by Django 4.2.10 on 2024-05-07 17:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='joined_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 7, 21, 10, 11, 468570)),
        ),
    ]
