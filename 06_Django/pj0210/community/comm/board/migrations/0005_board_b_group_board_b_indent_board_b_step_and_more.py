# Generated by Django 4.0.2 on 2022-02-10 05:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_board_b_img_alter_board_b_datd'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='b_group',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='board',
            name='b_indent',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='board',
            name='b_step',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='board',
            name='b_datd',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 10, 14, 43, 47, 406286)),
        ),
        migrations.AlterField(
            model_name='board',
            name='b_no',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
    ]
