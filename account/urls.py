from django.urls import path
from django.urls.resolvers import URLPattern
from .views import ajax_reg, entry, register, sign_out

urlpatterns = [
    path('register', register, name='register'),
    path('login', entry),
    path('logout', sign_out),
    path('ajax_reg', ajax_reg),
]
