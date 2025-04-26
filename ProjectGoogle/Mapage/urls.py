from django.urls import path
from . import views
app_name = 'Mapage'

urlpatterns = [
    path('home/', views.Main, name='index'),
    path('home/gmail/', views.gmail, name='gmail'),
    path('home/images/', views.Photos, name='images'),]