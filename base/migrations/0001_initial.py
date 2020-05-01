# Generated by Django 3.0.5 on 2020-05-01 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Access',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('role', models.CharField(choices=[('Company', 'Company'), ('MF', 'MF')], max_length=10, null=True)),
                ('area', models.CharField(choices=[('EMEA', 'EMEA'), ('Americas', 'Americas')], max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('code', models.CharField(max_length=30)),
                ('dateReceived', models.DateTimeField(auto_now_add=True)),
                ('dateUploaded', models.DateTimeField(auto_now_add=True)),
                ('area', models.CharField(choices=[('EMEA', 'EMEA'), ('Americas', 'Americas')], max_length=10)),
            ],
        ),
    ]
