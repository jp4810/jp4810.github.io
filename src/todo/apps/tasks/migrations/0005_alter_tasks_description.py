# Generated by Django 3.2.9 on 2021-11-26 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_tasks_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='description',
            field=models.TextField(default='', null=True),
        ),
    ]