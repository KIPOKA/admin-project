from django.urls import path
from . import views
app_name = 'car'

urlpatterns=[ 
    path('list/', views.list, name='list'),
    path('delete/', views.delete, name='delete'),
    path('add/', views.add, name='add')
]