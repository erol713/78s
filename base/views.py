from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
import json
from base.scrpits.dp import dpsum
from base.scrpits.dpw import dpword
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .models import Account
from .models import Access
from .forms import *
from .filters import *


@login_required(login_url='welcome')
def home(request):

    return render(request, 'base/index.html', {})


def welcome(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'username or password is incorect')

        return render(request, 'base/logIn/welcome.html', )


def logoutUser(request):
    logout(request)
    return redirect('welcome')


@login_required(login_url='welcome')
def addUser(request):

    userForm = CreateUserForm()
    accessForm = AccessForm()

    if request.method == 'POST':
        userForm = CreateUserForm(request.POST)
        accessForm = AccessForm(request.POST)

        if userForm.is_valid() and accessForm.is_valid():
            user = userForm.save(commit=False)
            access = accessForm.save(commit=False)
            access.username = user.username
            userForm.save()
            accessForm.save()

            return redirect('tech')

    context = {'userForm': userForm, 'accessForm': accessForm}
    return render(request, 'base/tech/addUser.html', context)


def addAccount(request):
    form = AccountForm()
    if request.method == 'POST':
        print(request.POST)
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tech')

    context = {'form': form}
    return render(request, 'base/tech/addAccount.html', context)


@login_required(login_url='welcome')
def upload(request):
    return render(request, 'base/uploadData/uploadData.html', {})


@login_required(login_url='welcome')
def uploadDownload(request):
    return render(request, 'base/uploadData/uploadDownload.html', {})


@login_required(login_url='welcome')
def reportUpload(request):
    return render(request, 'base/tech/reportUpload.html', {})


@login_required(login_url='welcome')
def overview(request):
    accounts = Account.objects.all()

    return render(request, 'base/MF/overview.html', {'accounts': accounts})


@login_required(login_url='welcome')
def tech(request):
    accounts = Account.objects.all()
    users = Access.objects.all()

    myAccessFilter = AccessFilter(request.GET, queryset=users)
    users = myAccessFilter.qs

    myAccountFilter = AccountFilter(request.POST, queryset=accounts)
    accounts = myAccountFilter.qs

    context = {'accounts': accounts, 'users': users,
               'myAccessFilter': myAccessFilter, 'myAccountFilter': myAccountFilter}

    return render(request, 'base/tech/techPanel.html', context)


def listAccounts(request):
    accounts = Account.objects.all()
    return render(request, 'base/listAccounts.html', {'accounts': accounts})


def test(request):
    return render(request, 'base/test.html', {})


def dp(request):
    response = dpsum(request)
    return JsonResponse(response, safe=False)


def dpw(request):
    response = dpword(request)
    return JsonResponse(response, safe=False)
