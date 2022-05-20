from django.urls import path
from .views import *

urlpatterns = [
    path('todo/', home, name = "home"),
    path('add/', Add, name = "ADDTODO"),
    path('delete/<int:pk>/', delete, name = "deletetodo")
]