# Generated by Django 2.0.7 on 2018-11-20 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_group_connection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='connection',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_connection.Connection'),
        ),
    ]
