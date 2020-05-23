from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenitcated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:

                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorised to view this page')
        return wrapper_func
    return decorator


def home_pages(view_func):
    def wrapper_func(request, *args, **kwargs):

        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'MF':
            return redirect('listAccounts')

        if group == 'Company':
            return redirect('uploadDownload')

        if group == 'admin':
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponse('You are not authorised to view this page')
    return wrapper_func
