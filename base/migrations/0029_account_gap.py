# Generated by Django 3.0.5 on 2020-05-31 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0028_access_filleddatacollection'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='gap',
            field=models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], max_length=30, null=True),
        ),
    ]