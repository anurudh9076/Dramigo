# Generated by Django 3.1.1 on 2021-05-17 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appoint', '0011_patient'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='appointments',
            new_name='appointment',
        ),
    ]
