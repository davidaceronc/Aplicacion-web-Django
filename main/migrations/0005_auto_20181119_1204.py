# Generated by Django 2.0.7 on 2018-11-19 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20181119_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authentication',
            name='connection',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_connection.Connection'),
        ),
    ]
