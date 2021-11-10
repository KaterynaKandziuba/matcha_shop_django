from django.urls import path
from django.urls.resolvers import URLPattern

from .views import register, login

urlpatterns = [
    path('register', register, name='register'),
    path('login', login, name='login')
]
