# Generated by Django 5.0.4 on 2024-04-18 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderinfo',
            name='status',
            field=models.CharField(default='0', help_text='Order status', max_length=1),
        ),
    ]
