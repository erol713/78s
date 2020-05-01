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
from .forms import CreateUserForm


@login_required(login_url='welcome')
def home(request):

    return render(request, 'base/index.html', {})


@login_required(login_url='welcome')
def overview(request):
    accounts = Account.objects.all()

    return render(request, 'base/MF/overview.html', {'accounts': accounts})


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
    if request.user.is_authenticated:
        return redirect('home')
    else:

        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'User added to the database' + user)

                return redirect('welcome')

        context = {'form': form}
        return render(request, 'base/tech/addUser.html', context)


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
def tech(request):
    return render(request, 'base/tech/techPanel.html', {})


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
