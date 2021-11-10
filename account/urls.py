from django.urls import path
from django.urls.resolvers import URLPattern
from .views import ajax_reg, entry, register, sign_out, login

urlpatterns = [
    path('register', register, name='register'),
    path('login', login, name='login'),
    path('entry', entry),
    path('sign_out', sign_out),
    path('ajax_reg', ajax_reg),
]
