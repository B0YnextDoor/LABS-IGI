# Generated by Django 5.0.4 on 2024-09-06 07:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutinfo',
            name='certificate',
            field=models.TextField(default='Default text', help_text="Company's certificate"),
        ),
        migrations.AddField(
            model_name='aboutinfo',
            name='history',
            field=models.TextField(default='Default text', help_text="Company's history"),
        ),
        migrations.AddField(
            model_name='aboutinfo',
            name='logo',
            field=models.ImageField(help_text="Company's logo", null=True, upload_to='app/static/about'),
        ),
        migrations.AddField(
            model_name='aboutinfo',
            name='requisites',
            field=models.TextField(default='Default text', help_text="Company's requisites"),
        ),
        migrations.AddField(
            model_name='aboutinfo',
            name='video',
            field=models.FileField(help_text='About video', null=True, upload_to='app/static/about', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])]),
        ),
    ]