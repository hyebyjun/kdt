# Generated by Django 4.0.2 on 2022-02-11 07:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='b_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2022, 2, 11, 16, 15, 28, 11474)),
        ),
    ]