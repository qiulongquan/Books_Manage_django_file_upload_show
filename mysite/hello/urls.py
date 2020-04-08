from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'hello'

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^upload', views.uploadImg),
    url(r'^show', views.showImg),
]
