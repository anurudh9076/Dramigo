# Generated by Django 3.1.1 on 2021-05-16 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appoint', '0006_auto_20210503_1728'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slots',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frm', models.TimeField()),
            ],
        ),
        migrations.AddField(
            model_name='doctor',
            name='slots',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='appoint.slots'),
        ),
    ]
