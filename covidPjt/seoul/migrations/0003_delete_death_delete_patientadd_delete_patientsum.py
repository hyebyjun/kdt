# Generated by Django 4.0.2 on 2022-03-08 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seoul', '0002_death'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Death',
        ),
        migrations.DeleteModel(
            name='Patientadd',
        ),
        migrations.DeleteModel(
            name='Patientsum',
        ),
    ]