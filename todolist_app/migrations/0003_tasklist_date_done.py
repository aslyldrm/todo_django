# Generated by Django 5.1.3 on 2024-11-26 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0002_tasklist_manager'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasklist',
            name='date_done',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
