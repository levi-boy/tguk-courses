from django.urls import path

from . import views


urlpatterns = [
    path('', views.main, name='main'),
    path('register/', views.register, name='register'),
    path('about/', views.about, name='about')
]