from django.urls import path
from . import views

urlpatterns = [
    path('', views.listmovie, name='listmovie'),
    path('addmovie/', views.addmovie, name='addmovie'),
]