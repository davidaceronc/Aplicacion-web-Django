# Generated by Django 2.0.7 on 2018-11-21 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_services', '0019_auto_20181120_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
