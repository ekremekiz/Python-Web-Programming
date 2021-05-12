from django.contrib import admin
from django.urls import path
from article import views

app_name = "article"

urlpatterns = [
    path('create/', views.index, name="index"),
]