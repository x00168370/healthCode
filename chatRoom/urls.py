from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views
from .views import *

app_name = "chatRoom"

urlpatterns= [
    path('admin/', admin.site.urls),


]