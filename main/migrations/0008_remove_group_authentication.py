# Generated by Django 2.0.7 on 2018-11-19 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20181119_1214'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='authentication',
        ),
    ]
