# Generated by Django 2.0.7 on 2018-11-17 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_services', '0004_auto_20181117_0950'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='button',
            name='services',
        ),
        migrations.RemoveField(
            model_name='button',
            name='widget',
        ),
        migrations.DeleteModel(
            name='Button',
        ),
    ]
