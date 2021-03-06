# Generated by Django 4.0.2 on 2022-02-11 06:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('member', '0002_alter_member_u_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('b_no', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('b_title', models.CharField(max_length=100)),
                ('b_content', models.TextField()),
                ('b_date', models.IntegerField(default=0)),
                ('b_group', models.IntegerField(default=0)),
                ('b_step', models.IntegerField(default=0)),
                ('b_indent', models.IntegerField(default=0)),
                ('b_hit', models.IntegerField(default=0)),
                ('b_img', models.ImageField(blank=True, upload_to='')),
                ('member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='member.member')),
            ],
        ),
    ]
