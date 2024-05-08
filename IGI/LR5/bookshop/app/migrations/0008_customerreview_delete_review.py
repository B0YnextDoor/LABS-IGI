# Generated by Django 5.0.4 on 2024-04-21 14:22

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_qa_options_remove_qa_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, help_text='Unique ID', primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, help_text='Creation date & time')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, help_text='Last update date & time')),
                ('rate', models.PositiveSmallIntegerField(help_text='Rate (0-5)')),
                ('text', models.TextField(help_text="Review's text")),
                ('user', models.ForeignKey(help_text='Reviewer', on_delete=django.db.models.deletion.CASCADE, to='app.customer')),
            ],
            options={
                'db_table': 'customer_reviews_table',
                'ordering': ['rate'],
            },
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]
