# Generated by Django 3.0.3 on 2020-08-09 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='project_title',
            field=models.TextField(null=True),
        ),
    ]