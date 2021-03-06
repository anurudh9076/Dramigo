# Generated by Django 3.1.1 on 2021-05-21 06:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appoint', '0015_auto_20210517_2302'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='slot',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appoint.slots'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateField(blank=True, default=False),
        ),
    ]
