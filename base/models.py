from django.db import models
from django.contrib.auth.models import User

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
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
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
    user = models.ForeignKey(Access, null=True, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=30)
    dateReceived = models.DateTimeField(auto_now_add=True)
    dateUploaded = models.DateTimeField(auto_now_add=True)
    area = models.CharField(max_length=10, choices=AREAS)

    # dataCollection
    # finalPack

    def __str__(self):
        return self.name
