# Generated by Django 2.0.7 on 2018-11-12 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_admin', '0016_auto_20181112_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='authentication',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_admin.Authentication'),
        ),
    ]
