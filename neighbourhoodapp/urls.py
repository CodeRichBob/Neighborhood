from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='hood-home'),
    path('all-hoods/',views.neighbourhoods,name='hood'),
]