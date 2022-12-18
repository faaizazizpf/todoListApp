from django.urls import path, include
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('add/', views.add, name='Add'),
    
    path('add/addrecord/', views.addrecord, name='Addrecord'),
]
