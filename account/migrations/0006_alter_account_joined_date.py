# Generated by Django 4.2.10 on 2024-05-08 14:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_account_joined_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='joined_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 8, 18, 16, 1, 174080)),
        ),
    ]
