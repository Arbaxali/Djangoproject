from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    # Home Page API's
    path('home1/',views.home), 
    path('gamemanager/', views.list),
    path('gamemanager_ins/', views.insert_view),
    path('/gamemanager_del/<id>', views.delete_view),
]


