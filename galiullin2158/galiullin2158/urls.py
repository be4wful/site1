from django.contrib import admin
from django.urls import path
from hi import views

urlpatterns = [
    path('', views.index),
    path('about', views.about, kwargs={'name': 'Amir', 'age': 16})

]
