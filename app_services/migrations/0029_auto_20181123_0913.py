# Generated by Django 2.0.7 on 2018-11-23 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_services', '0028_auto_20181122_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field',
            name='sql_query',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fields', to='app_services.SQLQuery'),
        ),
    ]
