# Generated by Django 4.2.4 on 2023-08-16 16:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('friends', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='relation',
            name='user_1',
        ),
        migrations.RemoveField(
            model_name='relation',
            name='user_2',
        ),
        migrations.AddField(
            model_name='relation',
            name='accepter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='accepter', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='relation',
            name='inviter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='inviter', to=settings.AUTH_USER_MODEL),
        ),
    ]