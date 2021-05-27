from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from django.conf import settings
# from .views import *
from  . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('base/',views.base, name='base'),
]