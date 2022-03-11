# Generated by Django 4.0.2 on 2022-02-18 06:13

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
        ('board', '0006_remove_board_b_datd_board_b_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='b_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 18, 15, 13, 35, 693849)),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('c_no', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('c_pw', models.CharField(max_length=10)),
                ('c_content', models.TextField()),
                ('c_date', models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 18, 15, 13, 35, 693849))),
                ('fboard', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='board.board')),
                ('member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='member.member')),
            ],
        ),
    ]