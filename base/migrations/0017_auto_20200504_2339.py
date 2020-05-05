# Generated by Django 3.0.5 on 2020-05-04 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_auto_20200504_2337'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='username',
        ),
        migrations.AddField(
            model_name='account',
            name='username',
            field=models.ManyToManyField(blank=True, null=True, related_name='cm', to='base.Access'),
        ),
    ]
