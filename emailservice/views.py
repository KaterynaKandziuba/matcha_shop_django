from django.shortcuts import render
from django.core.mail import send_mail

def newsletter(request):
    return render(request, 'home/newsletter.html')


def success(request):
    return render(request, 'home/success.html')


def failed(request):
    return render(request, 'home/failed.html')


def admin_page(request):
    return render(request, 'home/admin_page.html')