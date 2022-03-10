# Generated by Django 4.0.2 on 2022-03-03 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dailycovid',
            fields=[
                ('strdate', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('intdate', models.IntegerField(default=0)),
                ('deathCnt', models.IntegerField(default=0)),
                ('decideCnt', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='dailyvaccine',
            fields=[
                ('strdate', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('intdate', models.IntegerField(default=0)),
                ('firstCnt', models.IntegerField(default=0)),
                ('secondCnt', models.IntegerField(default=0)),
                ('thirdCnt', models.IntegerField(default=0)),
                ('totalFirstCnt', models.IntegerField(default=0)),
                ('totalSecondCnt', models.IntegerField(default=0)),
                ('totalThirdCnt', models.IntegerField(default=0)),
            ],
        ),
    ]