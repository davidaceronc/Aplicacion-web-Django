# Generated by Django 2.0.7 on 2018-11-23 03:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_services', '0025_auto_20181122_2157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sqlquery',
            name='description_fields',
        ),
        migrations.AddField(
            model_name='field',
            name='sql_query',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app_services.SQLQuery'),
        ),
    ]
