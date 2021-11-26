# Generated by Django 3.2.9 on 2021-11-26 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20211125_1412'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasks',
            name='update_at',
        ),
        migrations.AddField(
            model_name='tasks',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
