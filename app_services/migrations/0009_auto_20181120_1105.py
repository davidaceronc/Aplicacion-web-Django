# Generated by Django 2.0.7 on 2018-11-20 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_services', '0008_auto_20181120_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='widget',
            name='groups',
            field=models.ManyToManyField(blank=True, to='main.Group'),
        ),
    ]