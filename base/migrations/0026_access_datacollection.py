# Generated by Django 3.0.5 on 2020-05-09 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0025_auto_20200505_0001'),
    ]

    operations = [
        migrations.AddField(
            model_name='access',
            name='dataCollection',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]