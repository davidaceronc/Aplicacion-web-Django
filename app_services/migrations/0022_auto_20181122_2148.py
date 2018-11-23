# Generated by Django 2.0.7 on 2018-11-23 02:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_services', '0021_auto_20181120_2149'),
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('hidden', models.BooleanField(default=True)),
                ('ofType', models.CharField(choices=[('Int', 'Int'), ('String', 'String'), ('Boolean', 'Boolean')], max_length=20)),
                ('sql_query', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_services.SQLQuery')),
            ],
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name': 'Field', 'verbose_name_plural': 'Fields'},
        ),
        migrations.AlterField(
            model_name='menu',
            name='widget',
            field=models.OneToOneField(limit_choices_to={'ofType': 'menu'}, on_delete=django.db.models.deletion.CASCADE, to='app_services.Widget'),
        ),
    ]
