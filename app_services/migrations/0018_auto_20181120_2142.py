# Generated by Django 2.0.7 on 2018-11-21 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_services', '0017_auto_20181120_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='title',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]