# Generated by Django 3.0.5 on 2020-05-09 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0026_access_datacollection'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='finalPack',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
