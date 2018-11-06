# Generated by Django 2.1.3 on 2018-11-06 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_connection', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Icon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('image', models.ImageField(upload_to='icons')),
            ],
        ),
        migrations.CreateModel(
            name='Kind',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('description', models.CharField(blank=True, max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('description', models.CharField(blank=True, max_length=300)),
                ('longitude', models.CharField(max_length=100)),
                ('latitude', models.CharField(max_length=100)),
                ('icon', models.ForeignKey(blank=True, default=None, on_delete='PROTECTED', to='app_services.Icon')),
            ],
        ),
        migrations.CreateModel(
            name='MissingItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('description', models.CharField(max_length=200)),
                ('date', models.DateField(auto_now_add=True)),
                ('photo', models.ImageField(blank=True, upload_to='photos')),
            ],
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('extension', models.CharField(blank=True, max_length=50)),
                ('phone', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Permits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('student', models.BooleanField(default=False)),
                ('teacher', models.BooleanField(default=False)),
                ('clerk', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, unique=True)),
                ('state', models.BooleanField(default=False)),
                ('description', models.CharField(blank=True, max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='SQLQuery',
            fields=[
                ('service', models.OneToOneField(limit_choices_to={'kind': '4'}, on_delete='CASCADE', primary_key=True, related_name='query', related_query_name='query', serialize=False, to='app_services.Service')),
                ('type_name', models.CharField(max_length=50, unique=True)),
                ('query_sql', models.CharField(max_length=300)),
                ('description_fields', models.CharField(blank=True, max_length=300)),
                ('connection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_connection.Connection')),
            ],
            options={
                'verbose_name': 'Query',
                'verbose_name_plural': 'Queries',
            },
        ),
        migrations.AddField(
            model_name='service',
            name='icon',
            field=models.ForeignKey(on_delete='PROTECTED', to='app_services.Icon'),
        ),
        migrations.AddField(
            model_name='service',
            name='kind',
            field=models.ForeignKey(on_delete='PROTECTED', to='app_services.Kind'),
        ),
        migrations.AddField(
            model_name='service',
            name='permits',
            field=models.ForeignKey(on_delete='PROTECTED', to='app_services.Permits'),
        ),
        migrations.AddField(
            model_name='office',
            name='service',
            field=models.ForeignKey(limit_choices_to={'kind': '2'}, on_delete='CASCADE', related_name='offices', related_query_name='office', to='app_services.Service'),
        ),
        migrations.AddField(
            model_name='missingitem',
            name='service',
            field=models.ForeignKey(limit_choices_to={'kind': '1'}, on_delete='CASCADE', related_name='items', related_query_name='item', to='app_services.Service'),
        ),
        migrations.AddField(
            model_name='location',
            name='service',
            field=models.ForeignKey(limit_choices_to={'kind': '3'}, on_delete='CASCADE', related_name='locations', related_query_name='location', to='app_services.Service'),
        ),
    ]
