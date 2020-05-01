from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Access(models.Model):
    ROLES = (
        ('Company', 'Company'),
        ('MF', 'MF'),
    )

    AREAS = (
        ('EMEA', 'EMEA'),
        ('Americas', 'Americas'),
    )
    username = models.CharField(max_length=30, null=True)
    date = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=10, null=True, choices=ROLES)
    area = models.CharField(max_length=10, null=True, choices=AREAS)

    def __str__(self):
        return self.role


class Account(models.Model):

    AREAS = (
        ('EMEA', 'EMEA'),
        ('Americas', 'Americas'),
    )

    STATUS = (
        ('Data collection sent', 'Data collection sent'),
        ('Data Received', 'Data Received'),
        ('Analysis', 'Analysis'),
        ('Final Pack Uploaded', 'Final Pack Uploaded'),
    )
    username = models.ForeignKey(
        Access, blank=True,  null=True, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=30)
    dateReceived = models.DateTimeField(auto_now_add=True)
    dateUploaded = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=30, null=True, choices=STATUS)
    area = models.CharField(max_length=10, choices=AREAS)

    # dataCollection
    # finalPack

    def __str__(self):
        return self.name
