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
from django.contrib.auth.models import Group

from .models import Account
from .models import Access
from .forms import *
from .filters import *
from .decorators import unauthenitcated_user, allowed_users, home_pages
from django.template.loader import render_to_string, get_template


@login_required(login_url='welcome')
@home_pages
def home(request):
    accounts = Account.objects.all()
    users = Access.objects.all()
    total_accounts = accounts.count()

    delivered = accounts.filter(status='Final Pack Uploaded').count()
    analysis = accounts.filter(status='Analysis').count()
    gap = accounts.filter(gap='YES').count()

    myAccessFilter = AccessFilter(request.GET, queryset=users)
    users = myAccessFilter.qs

    myAccountFilter = AccountFilter(request.POST, queryset=accounts)
    accounts = myAccountFilter.qs

    context = {'accounts': accounts, 'users': users,
               'myAccessFilter': myAccessFilter, 'myAccountFilter': myAccountFilter,
               'total_accounts': total_accounts, 'delivered': delivered, 'analysis': analysis, 'gap': gap}

    return render(request, 'base/tech/techPanel.html', context)


@unauthenitcated_user
def welcome(request):

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
@allowed_users(allowed_roles=['admin'])
def addUser(request):

    userForm = CreateUserForm()
    accessForm = AccessForm()

    if request.method == 'POST':
        userForm = CreateUserForm(request.POST)
        accessForm = AccessForm(request.POST, request.FILES)

        if userForm.is_valid() and accessForm.is_valid():
            user = userForm.save(commit=False)
            access = accessForm.save(commit=False)
            access.username = user.username

            user = userForm.save()
            access = accessForm.save()

            group = Group.objects.get(name=access.role)
            user.groups.add(group)

            group = Group.objects.get(name=access.area)
            user.groups.add(group)

            return redirect('tech')

    context = {'userForm': userForm, 'accessForm': accessForm}
    return render(request, 'base/tech/addUser.html', context)


def deleteUser(request, pk):
    data = dict()
    user = Access.objects.get(id=pk)
    u = User.objects.get(username=user.username)
    if request.method == "POST":
        user.delete()
        u.delete()
        data['form_is_valid'] = True
        access = Access.objects.all()
        data['tech'] = render_to_string(
            'base/tech/usersList.html', {'access': access})
    else:
        context = {'item': user}
        data['html_form'] = render_to_string(
            'base/tech/deleteModal.html', context, request=request)

    return JsonResponse(data)


@allowed_users(allowed_roles=['admin'])
def addAccount(request):
    form = AccountForm()
    form.fields["username"].queryset = Access.objects.filter(role='MF')
    if request.method == 'POST':
        form = AccountForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tech')

    context = {'form': form}
    return render(request, 'base/tech/addAccount.html', context)


@allowed_users(allowed_roles=['admin'])
def businessUnits(request, pk):
    user = Access.objects.get(username=pk)

    form = AccountForm()
    form.fields["username"].queryset = Access.objects.filter(role='MF')

    if request.method == 'POST':
        form = AccountForm(request.POST, request.FILES,
                           instance=Account.objects.get(name=account))
        if form.is_valid():
            form.save()
            return redirect('tech')

    context = {'form': form, 'user': user}
    return render(request, 'base/tech/pickBU.html', context)


@allowed_users(allowed_roles=['admin'])
def dataCollection(request, pk):
    user = Access.objects.get(username=pk)

    form = dataCollectionForm()

    if request.method == 'POST':
        form1 = dataCollectionForm(request.POST, request.FILES,
                                   instance=Access.objects.get(username=user.username))

        if form1.is_valid():
            account = Account.objects.get(name=user.username)
            account.status = 'Data collection sent'
            account.save()
            form1.save()
            return redirect('tech')

    context = {'form': form, 'user': user}
    return render(request, 'base/tech/dataCollection.html', context)


@allowed_users(allowed_roles=['admin'])
def finalPack(request, pk):
    account = Account.objects.get(name=pk)
    form = AccountForm()
    if request.method == 'POST':

        form1 = finalPackForm(request.POST, request.FILES,
                              instance=Account.objects.get(name=account))
        if form1.is_valid():
            form1.instance.status = "Final Pack Uploaded"
            form1.save()
            return redirect('tech')

    context = {'form': form}
    return render(request, 'base/tech/finalPack.html', context)


@login_required(login_url='welcome')
@allowed_users(allowed_roles=['admin', 'Company'])
def upload(request):

    return render(request, 'base/uploadData/uploadData.html', )


@login_required(login_url='welcome')
@allowed_users(allowed_roles=['admin', 'Company'])
def uploadDownload(request):
    user = Access.objects.get(username=request.user)

    form = filledDataCollection()

    if request.method == 'POST':
        form1 = filledDataCollection(request.POST, request.FILES,
                                     instance=Access.objects.get(username=request.user))

        if form1.is_valid():
            account = Account.objects.get(name=request.user)
            account.status = 'Data Received'
            account.save()
            form1.save()

    context = {'user': user, 'form': form}
    return render(request, 'base/uploadData/uploadDownload.html', context)


@login_required(login_url='welcome')
@allowed_users(allowed_roles=['admin', 'MF', 'Company'])
def overview(request, pk):
    account = Account.objects.get(name=pk)

    return render(request, 'base/MF/overview.html', {'account': account})


@login_required(login_url='welcome')
@allowed_users(allowed_roles=['admin'])
def tech(request):
    accounts = Account.objects.all()
    users = Access.objects.all()
    print(accounts[0].finalPack)

    total_accounts = accounts.count()

    delivered = accounts.filter(status='Final Pack Uploaded').count()
    analysis = accounts.filter(status='Analysis').count()
    gap = accounts.filter(gap='YES').count()

    myAccessFilter = AccessFilter(request.GET, queryset=users)
    users = myAccessFilter.qs

    myAccountFilter = AccountFilter(request.POST, queryset=accounts)
    accounts = myAccountFilter.qs

    context = {'accounts': accounts, 'users': users,
               'myAccessFilter': myAccessFilter, 'myAccountFilter': myAccountFilter,
               'total_accounts': total_accounts, 'delivered': delivered, 'analysis': analysis, 'gap': gap}

    return render(request, 'base/tech/techPanel.html', context)


@allowed_users(allowed_roles=['admin', 'MF'])
def listAccounts(request):

    groups = request.user.groups.values_list('name', flat=True)

    if 'MF' in groups:
        accounts = Account.objects.filter(
            username__username__contains=request.user)
    else:
        accounts = Account.objects.all()

    myAccountFilter = AccountFilter(request.POST, queryset=accounts)
    accounts = myAccountFilter.qs

    return render(request, 'base/listAccounts.html', {'accounts': accounts, 'myAccountFilter': myAccountFilter})


@allowed_users(allowed_roles=['admin'])
def dataOverview(request):

    access = Access.objects.filter(role="Company")

    myAccessFilter = AccessFilter(request.POST, queryset=access)
    access = myAccessFilter.qs

    return render(request, 'base/tech/dataOverview.html', {'access': access, 'myAccessFilter': myAccessFilter})


def test(request):
    accounts = Account.objects.all()
    users = Access.objects.all()

    myAccessFilter = AccessFilter(request.GET, queryset=users)
    users = myAccessFilter.qs

    myAccountFilter = AccountFilter(request.POST, queryset=accounts)
    accounts = myAccountFilter.qs

    context = {'accounts': accounts, 'users': users,
               'myAccessFilter': myAccessFilter, 'myAccountFilter': myAccountFilter}
    return render(request, 'base/test.html', context)


def dp(request):
    response = dpsum(request)
    return JsonResponse(response, safe=False)


def dpw(request, pk):
    response = dpword(request)
    return JsonResponse(response, safe=False)
