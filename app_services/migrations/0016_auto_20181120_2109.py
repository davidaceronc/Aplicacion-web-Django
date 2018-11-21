# Generated by Django 2.0.7 on 2018-11-21 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_services', '0015_auto_20181120_1749'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='widget',
            name='description',
        ),
        migrations.RemoveField(
            model_name='widget',
            name='icon',
        ),
        migrations.AddField(
            model_name='menu',
            name='description',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='menu',
            name='icon',
            field=models.ForeignKey(default=None, on_delete='PROTECTED', to='app_services.Icon'),
        ),
    ]
