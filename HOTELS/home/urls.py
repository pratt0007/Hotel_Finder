from django.urls import path
from django.contrib import admin
from .views import *
urlpatterns = [
    path('',home,name ="home"),
    path('api/hotels', api_hotel)
    
]
