from django.urls import path
from django.urls.resolvers import URLPattern

from .views import admin_page, failed, newsletter, success

urlpatterns = [
    path('newsletter', newsletter),
    path('success', success),
    path('failed', failed),
    path('admin_page', admin_page),
]
