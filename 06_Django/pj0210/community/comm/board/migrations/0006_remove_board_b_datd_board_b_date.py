# Generated by Django 4.0.2 on 2022-02-10 06:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0005_board_b_group_board_b_indent_board_b_step_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='board',
            name='b_datd',
        ),
        migrations.AddField(
            model_name='board',
            name='b_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 10, 15, 29, 2, 878516)),
        ),
    ]
