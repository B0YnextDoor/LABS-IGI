# Generated by Django 5.0.4 on 2024-04-18 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_orderinfo_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderinfo',
            name='sale',
            field=models.PositiveSmallIntegerField(default=0, help_text="Order's sale"),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='status',
            field=models.CharField(default='0', help_text="Order's status", max_length=1),
        ),
    ]
