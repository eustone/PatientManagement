# Generated by Django 3.0.4 on 2021-07-06 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0004_auto_20210607_0436'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientrecord',
            name='age',
            field=models.CharField(default=1, max_length=3),
        ),
    ]