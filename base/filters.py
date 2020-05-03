import django_filters

from .models import *


class AccountFilter(django_filters.FilterSet):
    class Meta:
        model = Account
        fields = '__all__'
        exclude = ['username']


class AccessFilter(django_filters.FilterSet):
    class Meta:
        model = Access
        fields = '__all__'
        exclude = ['date']
