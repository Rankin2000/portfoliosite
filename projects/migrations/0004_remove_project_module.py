# Generated by Django 4.2.11 on 2024-08-25 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_project_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='module',
        ),
    ]
