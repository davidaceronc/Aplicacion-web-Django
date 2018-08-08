# Generated by Django 2.0.7 on 2018-08-06 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0008_service_class_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='items_search',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='service',
            name='type_service',
            field=models.CharField(blank=True, choices=[('list', 'Lista'), ('field', 'Único')], max_length=50),
        ),
    ]
