# Generated by Django 3.1.1 on 2021-05-21 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appoint', '0016_auto_20210521_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appoint.doctor'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.CharField(choices=[('cancelled', 'Cancelled'), ('pending', 'Pending'), ('completed', 'Completed')], default='pending', max_length=10, null=True),
        ),
    ]