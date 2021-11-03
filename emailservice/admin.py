from django.contrib import admin
from .models import Mailing, UserEmail, Feedback

admin.site.register(UserEmail)
admin.site.register(Feedback)
admin.site.register(Mailing)

