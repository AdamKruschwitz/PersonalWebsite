# Generated by Django 3.1.2 on 2020-11-24 03:18

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
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=1024)),
                ('github_link', models.CharField(max_length=128)),
                ('project_finished', models.BooleanField(default=False)),
            ],
        ),
    ]
