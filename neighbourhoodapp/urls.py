from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='hood-home'),
    path('all-hoods/',views.neighbourhoods,name='hood'),
    path('new-hood/', views.create_neighbourhood, name='new-hood'),
    path('join_hood/<id>', views.join_neighbourhood, name='join-hood'),
]