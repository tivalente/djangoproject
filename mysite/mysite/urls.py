from django.contrib import admin
from django.urls import include, path
from mysite.admin import admin_site

urlpatterns = [
    path("contacts/", include("contacts.urls")),
    path("polls/", include("polls.urls")),
    path("admin/", admin_site.urls),
]
