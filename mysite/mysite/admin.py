from django.contrib import admin
from polls.models import Choice, Question

# from .models import MyModel


class CustomAdminSite(admin.AdminSite):
    site_header = "Menu de Administração"


admin_site = CustomAdminSite()
admin_site.register(Choice)
admin_site.register(Question)
