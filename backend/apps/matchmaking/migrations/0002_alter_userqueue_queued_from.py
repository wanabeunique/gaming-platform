# Generated by Django 4.2.6 on 2024-02-05 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matchmaking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userqueue',
            name='queued_from',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
