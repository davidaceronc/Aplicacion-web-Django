# Generated by Django 2.1.4 on 2018-12-23 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20181222_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='authenticationdb',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='authenticationldap',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]