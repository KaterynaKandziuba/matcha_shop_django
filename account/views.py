from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse

def register(request):
    if request.method == 'GET':
        return render(request, 'account/register.html', context={
            'page_name': 'Registration',
            'page_app': 'account',
            'page_view': 'register'
        })
    elif request.method == 'POST':
        user_login = request.POST.get('login')
        user_password = request.POST.get('pwd')
        user_email = request.POST.get('email')

    user = User.objects.create_user(user_login, user_email, user_password)
    if user is None:
        mess = 'Registration failed :('
        color = 'red'
    else:
        user.save()
        mess = 'You are successfully registered!'
        color = 'green'

        return render(request, 'home/index.html', context={
            'page_name': 'Register',
            'page_app': 'account',
            'page_view': 'registration',
            'mess': mess,
            'color': color
        })

def entry(request):
    if request.method == 'GET':
        return render(request, 'account/login.html', context={
            'page_name': 'Login',
            'page_app': 'account',
            'page_view': 'login'
        })
    elif request.method == 'POST':
        user_login = request.POST.get('login')
        user_password = request.POST.get('pwd')

    user = authenticate(request, username=user_login, password=user_password)
    if user is None:
        mess = 'Wrong user name or password ...'
        color = 'orange'
        return render(request, 'account/report.html', context={
            'page_name': 'Login',
            'page_app': 'account',
            'page_view': 'report',
            'mess': mess,
            'color': color
        })
    else:
        login(request, user)
        return redirect('/')


def sign_out(request):
    logout(request)
    return render(request, 'home/index.html', context={
            'page_name': 'Logout',
            'page_app': 'account',
            'page_view': 'sign_out'
        })


def ajax_reg(request):
    response = dict()
    login = request.GET.get('login')
    try:
        User.objects.get(username=login)
        response['message'] = 'Busy'
    except User.DoesNotExist:
        response['message'] = 'Ок'
    return JsonResponse(response)
