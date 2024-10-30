# Generated by Django 5.0.4 on 2024-10-16 17:14

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_companypartner_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='BannerSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, help_text='Unique ID', primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, help_text='Creation date & time')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, help_text='Last update date & time')),
                ('loop', models.BooleanField(default=True)),
                ('navs', models.BooleanField(default=True)),
                ('auto', models.BooleanField(default=True)),
                ('stopMouseHover', models.BooleanField(default=True)),
                ('delay', models.FloatField(default=5.0)),
            ],
            options={
                'db_table': 'banner_settings_table',
                'ordering': ['id'],
            },
        ),
    ]