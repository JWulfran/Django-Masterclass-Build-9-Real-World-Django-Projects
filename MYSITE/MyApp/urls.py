from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'MyApp'

urlpatterns = [
    path('', views.index, name= 'index'),
    path('<int:id>/', views.detail, name='detail'),
    path('add/', views.create_item, name='create_item'),
    path('update/<int:id>/', views.update_item, name='update_item'),
    path('delete/<int:id>/', views.delete_item, name='delete_item'),
]