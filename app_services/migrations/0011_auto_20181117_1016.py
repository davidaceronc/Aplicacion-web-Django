# Generated by Django 2.0.7 on 2018-11-17 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_services', '0010_service_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='icon',
            field=models.ForeignKey(on_delete='PROTECTED', to='app_services.Icon'),
        ),
    ]