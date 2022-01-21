from django.contrib import admin
from django.urls import path
from . import views

app_name = 'user'
urlpatterns = [
    path('', views.index, name='home'),
    path('create', views.createuser),
    path('update/<id>', views.change),
    path('delete/<id>', views.delete)
]
