from django.contrib import admin

from .models import Profile


admin.site.register(Profile)
from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
