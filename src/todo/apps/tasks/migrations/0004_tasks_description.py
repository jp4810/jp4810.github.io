# Generated by Django 3.2.9 on 2021-11-26 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_auto_20211126_1308'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
