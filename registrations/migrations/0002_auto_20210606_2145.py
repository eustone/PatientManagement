# Generated by Django 3.0.4 on 2021-06-06 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientrecord',
            name='date_of_birth',
            field=models.DateTimeField(auto_now=True),
        ),
    ]