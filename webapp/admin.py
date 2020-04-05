from django.contrib import admin
from django.conf import settings
from .models import Countries


# Register your models here.
if settings.DEBUG:
    admin.site.register(Countries)
