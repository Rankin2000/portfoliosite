# Generated by Django 3.0.3 on 2020-05-25 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('module', models.CharField(max_length=6)),
                ('image', models.FilePathField(path='/img')),
            ],
        ),
    ]
