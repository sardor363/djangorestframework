# Generated by Django 3.1.14 on 2022-06-23 14:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('celebs', '0002_auto_20220622_1717'),
    ]

    operations = [
        migrations.AddField(
            model_name='celebs',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user', verbose_name='Пользователь'),
            preserve_default=False,
        ),
    ]
