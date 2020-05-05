# Generated by Django 3.0.5 on 2020-05-04 23:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0019_auto_20200504_2342'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='user',
        ),
        migrations.AddField(
            model_name='account',
            name='username',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='cm', to=settings.AUTH_USER_MODEL),
        ),
    ]
