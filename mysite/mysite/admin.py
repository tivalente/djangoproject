from django.contrib import admin

# from .models import MyModel


class CustomAdminSite(admin.AdminSite):
    site_header = "Menu de Administração"


admin_site = CustomAdminSite()
# admin_site.register(MyModel)
